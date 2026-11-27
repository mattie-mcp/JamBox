# JamBox

Smart NFC-based music player for toddlers. Slide a chunky cartridge into the box, music plays; pull it out, music pauses. Built for Jamie.

## Architecture
- **Backend**: Python 3.11+ (FastAPI) - NFC daemon + REST API
- **Frontend**: Next.js 16 (App Router), built as a static export and served by FastAPI; parent management UI
- **Database**: SQLite via SQLAlchemy
- **Hardware (v2)**: Raspberry Pi 4, HiFiBerry Amp4 + 2 wired 3" drivers, PN532 NFC reader, slot microswitch, arcade buttons + rotary encoder, WS2812B 8x8 LED matrix, USB-C PD (15 V) power. See `docs/hardware.md` and `docs/enclosure.md`
- **Spotify**: Raspotify (Connect device) + Spotify Web API (playback control)

## Commands
- Backend: `cd backend && python -m pytest` (tests), `uvicorn app.main:app --reload` (dev server)
- Frontend: `cd frontend && npm run dev` (dev server), `npm test` (tests), `npm run build` (static export to `out/`)
- Deploy UI: `scripts/deploy-ui.sh` (run on the laptop; builds the UI and rsyncs `frontend/out/` to the Pi)
- NFC Daemon: `cd backend && python -m app.nfc_daemon` (requires hardware)

## Key Decisions
- The box is self-sufficient: all services run on the Pi except the UI build. No Node on the Pi, and no separate home server (it would only host static files while adding a second machine and cross-origin problems)
- SQLite is sufficient for single-device prototype
- Spotify Web API controls playback on the Pi's Raspotify/librespot instance
- Audio is wired (I2S amp), not Bluetooth; v2 software changes are tracked in `docs/plans/2026-11-24-hardwired-v2.md`
- Toddler safety: no magnets, no internal battery, volume capped in software
- Web app is local-network only. No CORS (same origin as the API). Playback endpoints are loopback-only. The volume hard cap lives in the backend `.env`. A settings PIN is required before any settings endpoint ships
