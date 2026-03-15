from datetime import datetime, timedelta
from unittest.mock import MagicMock

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base
from app.models import DiscoveryState
from app.nfc_daemon import check_discovery_mode, format_tag_id, handle_discovery


def test_format_tag_id():
    raw = bytes([0x04, 0xA2, 0x3B, 0x5C])
    assert format_tag_id(raw) == "04:A2:3B:5C"


def test_format_tag_id_single_byte():
    raw = bytes([0x0F])
    assert format_tag_id(raw) == "0F"


def _make_db():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def test_check_discovery_mode_active():
    db = _make_db()
    state = DiscoveryState(
        id=1,
        active=True,
        started_at=datetime.utcnow(),
        timeout_seconds=30,
    )
    db.add(state)
    db.commit()
    result = check_discovery_mode(db)
    assert result is not None
    assert result.active is True


def test_check_discovery_mode_expired():
    db = _make_db()
    state = DiscoveryState(
        id=1,
        active=True,
        started_at=datetime.utcnow() - timedelta(seconds=60),
        timeout_seconds=30,
    )
    db.add(state)
    db.commit()
    result = check_discovery_mode(db)
    assert result is None
    db.refresh(state)
    assert state.active is False


def test_check_discovery_mode_inactive():
    db = _make_db()
    state = DiscoveryState(id=1, active=False)
    db.add(state)
    db.commit()
    result = check_discovery_mode(db)
    assert result is None


def test_handle_discovery_stores_tag():
    db = _make_db()
    state = DiscoveryState(
        id=1,
        active=True,
        started_at=datetime.utcnow(),
        timeout_seconds=30,
    )
    db.add(state)
    db.commit()
    handle_discovery(db, state, "04:A2:3B:5C")
    db.refresh(state)
    assert state.detected_tag_id == "04:A2:3B:5C"
    assert state.active is False
