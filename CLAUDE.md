# JamBox

Smart NFC-based music player for toddlers. Slide a chunky cartridge into the box, music plays; pull it out, music pauses. Built for Jamie.

## Architecture
- **Backend**: Python 3.11+ (FastAPI) - NFC daemon + REST API
- **Frontend**: Next.js 14 (App Router) - parent management UI
- **Database**: SQLite via SQLAlchemy
- **Hardware (v2)**: Raspberry Pi 4, HiFiBerry Amp4 + 2 wired 3" drivers, PN532 NFC reader, slot microswitch, arcade buttons + rotary encoder, WS2812B 8x8 LED matrix, USB-C PD (15 V) power. See `docs/hardware.md` and `docs/enclosure.md`
- **Spotify**: Raspotify (Connect device) + Spotify Web API (playback control)

## Commands
- Backend: `cd backend && python -m pytest` (tests), `uvicorn app.main:app --reload` (dev server)
- Frontend: `cd frontend && npm run dev` (dev server), `npm test` (tests)
- NFC Daemon: `cd backend && python -m app.nfc_daemon` (requires hardware)

## Key Decisions
- All services run on the Raspberry Pi
- SQLite is sufficient for single-device prototype
- Spotify Web API controls playback on the Pi's Raspotify/librespot instance
- Audio is wired (I2S amp), not Bluetooth; v2 software changes are tracked in `docs/plans/2026-11-24-hardwired-v2.md`
- Toddler safety: no magnets, no internal battery, volume capped in software
- Web app is local-network only (no auth needed for prototype, revisit if exposing)
