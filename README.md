# JamBox

A smart NFC-based music player for toddlers. Slide a chunky wooden cartridge into the box and the matching Spotify song plays; pull it out and it pauses.

Inspired by [Tonie Box](https://tonies.com). Built for Jamie.

## How It Works

1. NFC tags are sealed inside chunky cartridges (wooden blocks)
2. A Raspberry Pi with an NFC reader detects which cartridge is in the slot
3. The Pi looks up the tag-to-song mapping and triggers Spotify playback through built-in speakers
4. Volume knob, Back / Play-Pause / Skip buttons and a dancing LED display are on the box
5. Parents manage mappings through a web app

## Components

| Component | Tech |
|-----------|------|
| Brain | Raspberry Pi 4 |
| Audio | HiFiBerry Amp4 + 2× 3" full-range drivers |
| NFC Reader | PN532 (I2C) + slot microswitch |
| Controls / display | Arcade buttons, rotary encoder, WS2812B 8×8 matrix |
| Power | Single USB-C PD charger (15 V) |
| Backend | Python / FastAPI |
| Frontend | Next.js / Tailwind |
| Database | SQLite |
| Music | Spotify Premium + Raspotify |

## Quick Start

See the [Hardware Guide](docs/hardware.md) for the parts list and wiring, and the [Enclosure Design](docs/enclosure.md) for the box, cartridges and design concepts.

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
