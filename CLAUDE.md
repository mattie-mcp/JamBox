# Music Box

Smart NFC-based music player for toddlers. Place a toy on the pedestal, music plays.

## Architecture
- **Backend**: Python 3.11+ (FastAPI) - NFC daemon + REST API
- **Frontend**: Next.js 14 (App Router) - parent management UI
- **Database**: SQLite via SQLAlchemy
- **Hardware**: Raspberry Pi 4/5, PN532 NFC reader, Bluetooth speaker
- **Spotify**: Raspotify (Connect device) + Spotify Web API (playback control)

## Commands
- Backend: `cd backend && python -m pytest` (tests), `uvicorn app.main:app --reload` (dev server)
- Frontend: `cd frontend && npm run dev` (dev server), `npm test` (tests)
- NFC Daemon: `cd backend && python -m app.nfc_daemon` (requires hardware)

## Key Decisions
- All services run on the Raspberry Pi
- SQLite is sufficient for single-device prototype
- Spotify Web API controls playback on the Pi's Raspotify instance
- Web app is local-network only (no auth needed for prototype, revisit if exposing)
