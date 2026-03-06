"""
NFC Listener Daemon

Polls the NFC reader and triggers playback via the API when a tag is detected.
Run on the Raspberry Pi: python -m app.nfc_daemon
"""

import time
import logging
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


def run():
    """Main loop - requires nfcpy and hardware."""
    try:
        import nfc
    except ImportError:
        logger.error("nfcpy not installed. Run: pip install nfcpy")
        return

    last_tag = None
    last_tag_time = 0
    debounce_seconds = 5  # Don't re-trigger same tag within 5s

    def on_connect(tag):
        nonlocal last_tag, last_tag_time
        tag_id = format_tag_id(tag.identifier)
        now = time.time()

        if tag_id == last_tag and (now - last_tag_time) < debounce_seconds:
            return True  # Keep listening, ignore duplicate

        logger.info(f"Tag detected: {tag_id}")
        last_tag = tag_id
        last_tag_time = now
        trigger_play(tag_id)
        return True  # Keep listening

    with nfc.ContactlessFrontend("tty:S0") as clf:
        logger.info("NFC daemon started. Waiting for tags...")
        while True:
            clf.connect(rdwr={"on-connect": on_connect})
            time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    run()
