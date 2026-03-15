"""
NFC Listener Daemon

Polls the NFC reader and triggers playback via the API when a tag is detected.
Supports discovery mode: when active, detected tag IDs are stored for registration
instead of triggering playback.

Run on the Raspberry Pi: python -m app.nfc_daemon
"""

import time
import logging
from datetime import datetime

import httpx

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
logger = logging.getLogger(__name__)

API_BASE = "http://localhost:8000"
POLL_INTERVAL = 0.5  # seconds


def trigger_play(tag_id: str) -> None:
    """Call the local API to play the track mapped to this tag."""
    try:
        response = httpx.post(f"{API_BASE}/api/play/{tag_id}", timeout=5)
        if response.status_code == 200:
            data = response.json()
            logger.info(f"Playing: {data['name']}")
        elif response.status_code == 404:
            logger.warning(f"No mapping for tag: {tag_id}")
        else:
            logger.error(f"API error: {response.status_code}")
    except httpx.RequestError as e:
        logger.error(f"Could not reach API: {e}")


def format_tag_id(tag_bytes: bytes) -> str:
    """Convert raw tag bytes to colon-separated hex string."""
    return ":".join(f"{b:02X}" for b in tag_bytes)


def check_discovery_mode(db_session):
    """Check if discovery mode is active. Returns the state row if active, else None."""
    from app.models import DiscoveryState

    state = db_session.query(DiscoveryState).filter(DiscoveryState.id == 1).first()
    if state and state.active and state.started_at:
        elapsed = (datetime.utcnow() - state.started_at).total_seconds()
        if elapsed > state.timeout_seconds:
            state.active = False
            state.detected_tag_id = None
            db_session.commit()
            return None
        return state
    return None


def handle_discovery(db_session, state, tag_id: str) -> None:
    """Record discovered tag and deactivate discovery mode."""
    state.detected_tag_id = tag_id
    state.active = False
    db_session.commit()
    logger.info(f"Discovery mode: captured tag {tag_id}")


def run():
    """Main loop - requires adafruit-circuitpython-pn532 and hardware."""
    try:
        import board
        import busio
        from adafruit_pn532.i2c import PN532_I2C
    except ImportError:
        logger.error(
            "Adafruit PN532 library not installed. "
            "Run: pip install adafruit-circuitpython-pn532"
        )
        return

    from app.database import SessionLocal

    i2c = busio.I2C(board.SCL, board.SDA)
    pn532 = PN532_I2C(i2c)
    logger.info(f"PN532 firmware: {pn532.firmware_version}")
    pn532.SAM_configuration()

    last_tag = None
    last_tag_time = 0
    debounce_seconds = 5  # Don't re-trigger same tag within 5s

    logger.info("NFC daemon started. Waiting for tags...")
    while True:
        uid = pn532.read_passive_target(timeout=POLL_INTERVAL)
        if uid is None:
            continue

        tag_id = format_tag_id(uid)
        now = time.time()

        if tag_id == last_tag and (now - last_tag_time) < debounce_seconds:
            continue

        last_tag = tag_id
        last_tag_time = now

        db = SessionLocal()
        try:
            state = check_discovery_mode(db)
            if state:
                handle_discovery(db, state, tag_id)
                continue
        finally:
            db.close()

        logger.info(f"Tag detected: {tag_id}")
        trigger_play(tag_id)


if __name__ == "__main__":
    run()
