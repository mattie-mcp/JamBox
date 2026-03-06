import os
from unittest.mock import patch, MagicMock

from fastapi.testclient import TestClient


def test_login_redirects():
    with patch.dict(os.environ, {
        "SPOTIPY_CLIENT_ID": "test_id",
        "SPOTIPY_CLIENT_SECRET": "test_secret",
    }):
        from app.main import app
        client = TestClient(app, follow_redirects=False)
        response = client.get("/auth/login")
        assert response.status_code in (302, 307)
        assert "accounts.spotify.com" in response.headers["location"]


def test_callback_without_code_returns_error():
    from app.main import app
    client = TestClient(app, follow_redirects=False)
    response = client.get("/auth/callback")
    assert response.status_code == 400
