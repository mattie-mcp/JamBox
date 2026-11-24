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

- **Inputs:** the slot microswitch (GPIO 5, via `gpiozero`) is the primary presence signal. NFC polling
  provides the tag ID and backs up the switch (treat ~3 consecutive misses as removed if the switch fails).
- **Insert:** read the tag. If it's the **same tag as last time and less than ~30 min ago**, resume. Otherwise
  play the mapped track from the start. An unknown tag shows the "?" LED state; discovery mode still works.
- **Remove:** call a new `POST /api/pause` and remember `{tag, position, time}` for resume.
- Keep the logic in pure functions (state transitions) so it's unit-testable without hardware,
  matching the existing `tests/test_nfc.py` style.

## 3. Controls daemon (new: `backend/app/controls.py`)

- `gpiozero.RotaryEncoder` on GPIO 17/27 sets the ALSA mixer volume, clamped to `MAX_VOLUME`.
  `gpiozero.Button` handles the encoder push (mute) and Back/Play-Pause/Skip on GPIO 23/24/25, with debounce.
- New API endpoints: `POST /api/pause`, `/api/resume`, `/api/next`, `/api/previous`, `/api/volume`.
  Thin wrappers over `spotify.py` (pause already exists).
- Settings (in SQLite, editable in the web UI): `max_volume`, `default_volume`, `led_brightness`,
  `resume_window_minutes`.
- New systemd unit: `scripts/jambox-controls.service`.

## 4. LED service (new: `backend/app/leds.py`)

- `rpi_ws281x` over SPI (GPIO 10). Needs `core_freq=500` / `core_freq_min=500` on the Pi 4.
- Spectrum: an ALSA `multi`/`dmix` + `snd-aloop` route so audio goes to both the Amp4 and the loopback.
  **cava** reads the loopback with raw output (8 bars) into a FIFO, and the LED service reads the FIFO.
- States: booting, idle glow, playing (spectrum), paused, unknown cartridge, volume overlay.
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

## Docs

- Update `docs/hardware.md` §6 once `pi-setup.sh` has been rewritten.
- README / CLAUDE.md already describe v2 hardware.
