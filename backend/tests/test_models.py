from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.database import Base
from app.models import TagMapping


def test_create_tag_mapping():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        mapping = TagMapping(
            tag_id="04:A2:3B:5C:6D:7E:80",
            spotify_uri="spotify:track:6rqhFgbbKwnb9MLmUQDhG6",
            name="Wheels on the Bus",
        )
        session.add(mapping)
        session.commit()

        result = session.query(TagMapping).first()
        assert result is not None
        assert result.tag_id == "04:A2:3B:5C:6D:7E:80"
        assert result.spotify_uri == "spotify:track:6rqhFgbbKwnb9MLmUQDhG6"
        assert result.name == "Wheels on the Bus"
        assert result.created_at is not None


def test_tag_id_is_unique():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        m1 = TagMapping(tag_id="AA:BB", spotify_uri="spotify:track:abc", name="Song 1")
        m2 = TagMapping(tag_id="AA:BB", spotify_uri="spotify:track:def", name="Song 2")
        session.add(m1)
        session.commit()
        session.add(m2)
        try:
            session.commit()
            assert False, "Should have raised IntegrityError"
        except Exception:
            session.rollback()
