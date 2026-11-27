# JamBox v2 software plan: hardwired box

**Status:** proposed, not started. The hardware is in [../hardware.md](../hardware.md) and the
physical design in [../enclosure.md](../enclosure.md).

v2 replaces the Bluetooth speaker with an I2S amp (HiFiBerry Amp4) and adds cartridges (insert/remove),
physical controls and an LED display. These are the software changes it needs.

## 1. Audio: Bluetooth → wired I2S

- `scripts/jambox-spotify.service`: switch librespot from `--backend pulseaudio` (PipeWire/Bluetooth)
  to `--backend alsa` and point it at the Amp4 device. Run it as a system service; it doesn't need a user session.
- Use `--volume-ctrl fixed` so phones on the network can't override the box's volume. The **knob**
  owns volume through the ALSA mixer (see §3).
- Add `--onevent` to report play/pause/track changes to the API (for the LEDs and the resume logic).
- `scripts/pi-setup.sh`: remove the Bluetooth and PipeWire steps. Add the `config.txt` lines from hardware.md §4
  and the `snd-aloop` module (for the visualizer).
- Remove the Bluetooth pairing docs everywhere (done in hardware.md).

## 2. Cartridge insert/remove (`backend/app/nfc_daemon.py`)

Today the daemon only reacts to a tag *appearing*, with a 5 s debounce. v2 needs a presence
state machine:

```
EMPTY ── switch closed / tag seen ──► READING ── tag id ──► PLAYING(tag)
  ▲                                                     │
  └──── switch open (or N consecutive NFC misses) ◄─────┘  → pause
```

- **Inputs:** NFC polling is the presence signal by default. Treat ~2–3 consecutive misses as "removed",
  and make the count configurable. If the optional slot microswitch (GPIO 5) is fitted, it becomes the primary
  signal for instant removal and NFC just identifies the tag. Design the state machine so either input works.
- **Insert:** read the tag. If it's the **same tag as last time and less than ~30 min ago** (decided), resume. Otherwise
  play the mapped track from the start. An unknown tag shows the "?" LED state; discovery mode still works.
- **Two tags per cartridge** (one under each face, decided 2026-11-27). Both tag IDs map to the same song, so
  either can identify the cartridge. Treat a second tag that maps to the same song as the same cartridge (no
  restart). The web app should make registering the second tag easy ("flip it and insert again").
- **Remove:** call a new `POST /api/pause` and remember `{tag, position, time}` for resume.
- Keep the logic in pure functions (state transitions) so it's unit-testable without hardware,
  matching the existing `tests/test_nfc.py` style.

## 3. Controls daemon (new: `backend/app/controls.py`)

- `gpiozero.RotaryEncoder` on GPIO 17/27 sets the ALSA mixer volume, clamped to `MAX_VOLUME`.
  `gpiozero.Button` handles the encoder push (mute) and Back/Play-Pause/Skip on GPIO 23/24/25, with debounce.
- New API endpoints: `POST /api/pause`, `/api/resume`, `/api/next`, `/api/previous`, `/api/volume`.
  Thin wrappers over `spotify.py` (pause already exists).
- Settings (in SQLite, editable in the web UI): `max_volume` (**parent-adjustable, default ≈ 80 dB**; decided;
  always clamped server-side to the hard cap, see §7),
  `default_volume`, `led_brightness`, `resume_window_minutes`.
- New systemd unit: `scripts/jambox-controls.service`.

## 4. LED service (new: `backend/app/leds.py`)

- `rpi_ws281x` over SPI (GPIO 10). Needs `core_freq=500` / `core_freq_min=500` on the Pi 4.
- Spectrum: an ALSA `multi`/`dmix` + `snd-aloop` route so audio goes to both the Amp4 and the loopback.
  **cava** reads the loopback with raw output (**5 bars**, ~30 fps, bass→treble) into a FIFO, and the LED service reads the FIFO.
- Matrix: Adafruit NeoPixel Shield 5×8 (#1430), 40 LEDs, mounted **portrait (5 wide × 8 tall)**. The shield is wired as 8 × 5 rows,
  so the service maps (x, y) → index with a 90° rotation; keep the mapping in one config so a different panel is a config change.
- Jukebox look (see enclosure.md "LED display"): warm palette only (amber → orange → red up each bar), peak dots that hold
  ~0.3 s then fall, a bass-beat flash on the bottom row, a left-to-right "tuning sweep" on cartridge insert, a 5×8 "?" glyph
  for unknown cartridges, and a 0–8 row volume overlay.
- States: booting (valves warming), idle glow, tuning sweep, playing (5-band equaliser), paused, unknown cartridge, volume overlay.
  It gets state from the API (or a small local socket) rather than polling Spotify.
- Brightness capped by the `led_brightness` setting (default ~20%).
- New systemd unit: `scripts/jambox-leds.service`, started early so the boot animation shows.

## 5. Reliability

- Enable the **overlay (read-only) root filesystem** once provisioning is done.
- Move the SQLite DB and the Spotify token cache to a small writable partition (or `/boot/firmware`-adjacent
  data partition) and configure `DATABASE_URL` accordingly. Use SQLite WAL mode.
- All services get `Restart=always`. The web UI should show service health.

## 6. Web UI

- Settings page: max volume, LED brightness, resume window.
- Tag registration copy: "insert the cartridge" instead of "tap the toy".

## 7. Web UI hosting and safety (decided 2026-11-27, built)

- **Static UI:** the Next.js app is a static export (`output: "export"`). It is built on a laptop or in CI
  and copied to the Pi with `scripts/deploy-ui.sh`. FastAPI serves `frontend/out` at `/` on port 8000,
  same origin as the API (`JAMBOX_UI_DIR` overrides the path). No Node runs on the Pi; `jambox-web` is gone.
- **Rejected: a separate home server for the UI.** The box must be self-sufficient: mappings, the Spotify
  token, volume limits and discovery all live on the Pi. A home server would only host static files, while
  adding a second machine, cross-origin/HTTPS problems, and no UI away from home.
- **Pi:** stays a 4 GB Pi 4. About 1 GB is used; the rest is long-term headroom.
- **Safety rules:**
  - `POST /api/play/{tag_id}` only accepts loopback requests (NFC daemon, buttons). Other LAN machines get 403.
  - CORS is off. Local dev sets `JAMBOX_DEV_CORS_ORIGINS=http://localhost:3000`.
  - Hard volume cap `JAMBOX_MAX_VOLUME_PERCENT` (default 60) lives only in the backend `.env`. No API can change it.
  - Before every play the backend lowers the device volume to the cap. If it can't, playback doesn't start.
- **TODO (design only):**
  - A parent settings PIN or pairing token, required for every settings write.
  - Settings writes (e.g. the parent `max_volume`) are always clamped to the hard cap.
  - A second volume limit at the ALSA/librespot level.
  - A versioned API (`/api/v1` plus `/api/v1/info`) if the UI and the box ever ship on different schedules.

## Docs

- Update `docs/hardware.md` §6 once `pi-setup.sh` has been rewritten.
- README / CLAUDE.md already describe v2 hardware.
