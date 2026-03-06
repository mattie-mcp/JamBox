from unittest.mock import patch, MagicMock

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
import app.models  # noqa: F401 - ensure models registered with Base
from app.main import app


def get_test_db():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    TestSession = sessionmaker(bind=engine)

    def override():
        db = TestSession()
        try:
            yield db
        finally:
            db.close()

    return override


def setup_client():
    override = get_test_db()
    app.dependency_overrides[get_db] = override
    return TestClient(app)


def test_create_mapping():
    client = setup_client()
    response = client.post(
        "/api/mappings",
        json={
            "tag_id": "04:A2:3B:5C:6D:7E:80",
            "spotify_uri": "spotify:track:abc123",
            "name": "Wheels on the Bus",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["tag_id"] == "04:A2:3B:5C:6D:7E:80"
    assert data["name"] == "Wheels on the Bus"
    assert "id" in data


def test_list_mappings():
    client = setup_client()
    client.post(
        "/api/mappings",
        json={"tag_id": "AA:BB", "spotify_uri": "spotify:track:1", "name": "Song 1"},
    )
    client.post(
        "/api/mappings",
        json={"tag_id": "CC:DD", "spotify_uri": "spotify:track:2", "name": "Song 2"},
    )
    response = client.get("/api/mappings")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_delete_mapping():
    client = setup_client()
    create = client.post(
        "/api/mappings",
        json={"tag_id": "AA:BB", "spotify_uri": "spotify:track:1", "name": "Song 1"},
    )
    mapping_id = create.json()["id"]
    response = client.delete(f"/api/mappings/{mapping_id}")
    assert response.status_code == 204

    response = client.get("/api/mappings")
    assert len(response.json()) == 0


def test_update_mapping():
    client = setup_client()
    create = client.post(
        "/api/mappings",
        json={"tag_id": "AA:BB", "spotify_uri": "spotify:track:1", "name": "Song 1"},
    )
    mapping_id = create.json()["id"]
    response = client.put(
        f"/api/mappings/{mapping_id}",
        json={"spotify_uri": "spotify:track:2", "name": "Song 2"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Song 2"
    assert response.json()["spotify_uri"] == "spotify:track:2"


def test_duplicate_tag_returns_409():
    client = setup_client()
    client.post(
        "/api/mappings",
        json={"tag_id": "AA:BB", "spotify_uri": "spotify:track:1", "name": "Song 1"},
    )
    response = client.post(
        "/api/mappings",
        json={"tag_id": "AA:BB", "spotify_uri": "spotify:track:2", "name": "Song 2"},
    )
    assert response.status_code == 409


def test_search_tracks():
    client = setup_client()
    mock_spotify = MagicMock()
    mock_spotify.search.return_value = {
        "tracks": {
            "items": [
                {
                    "uri": "spotify:track:abc",
                    "name": "Baby Shark",
                    "artists": [{"name": "Pinkfong"}],
                    "album": {"images": [{"url": "https://img.jpg"}]},
                }
            ]
        }
    }
    with patch("app.api.get_spotify", return_value=mock_spotify):
        response = client.get("/api/search?q=baby+shark")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Baby Shark"
