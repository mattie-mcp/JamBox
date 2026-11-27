from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR / 'jambox.db'}")

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI", "http://127.0.0.1:8000/auth/callback")
SPOTIFY_DEVICE_NAME = os.getenv("SPOTIFY_DEVICE_NAME", "raspotify")

# Parent web UI: the static export of the Next.js app (`npm run build` -> frontend/out).
UI_DIR = Path(os.getenv("JAMBOX_UI_DIR", str(BASE_DIR.parent / "frontend" / "out")))

# CORS is off in production: the UI is served from the same origin as the API.
# For `npm run dev` on a laptop, set e.g. JAMBOX_DEV_CORS_ORIGINS=http://localhost:3000
DEV_CORS_ORIGINS = [
    o.strip() for o in os.getenv("JAMBOX_DEV_CORS_ORIGINS", "").split(",") if o.strip()
]


def _hard_volume_cap() -> int:
    """Hard ceiling for Spotify volume (percent). Set only in the box's .env file;
    no API endpoint can raise it. Defaults low; clamped to 0-100."""
    try:
        value = int(os.getenv("JAMBOX_MAX_VOLUME_PERCENT", "60"))
    except ValueError:
        value = 60
    return max(0, min(100, value))


MAX_VOLUME_PERCENT = _hard_volume_cap()
