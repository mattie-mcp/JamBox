# JamBox

A smart NFC-based music player for toddlers. Place a toy on the pedestal, and the matching Spotify song plays automatically.

Inspired by [Tonie Box](https://tonies.com). Built for Jamie.

## How It Works

1. NFC tags are embedded in small toys
2. A Raspberry Pi with an NFC reader detects which toy is placed on the pedestal
3. The Pi looks up the tag-to-song mapping and triggers Spotify playback
4. Parents manage mappings through a web app

## Components

| Component | Tech |
|-----------|------|
| Brain | Raspberry Pi 4 |
| NFC Reader | PN532 (I2C) |
| Backend | Python / FastAPI |
| Frontend | Next.js / Tailwind |
| Database | SQLite |
| Music | Spotify Premium + Raspotify |

## Quick Start

See [Hardware Guide](docs/hardware.md) for shopping list and wiring.

### Development (on your Mac)

```bash
# Backend
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env  # Fill in Spotify credentials
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

### Raspberry Pi

```bash
git clone <repo> ~/music-box
cd ~/music-box
./scripts/pi-setup.sh
```

## Spotify Setup

1. Go to https://developer.spotify.com/dashboard
2. Create an app, get Client ID and Secret
3. Add `http://<pi-ip>:8000/callback` as a Redirect URI
4. Copy credentials to `backend/.env`
5. Visit `http://<pi-ip>:8000/auth/login` to authenticate
