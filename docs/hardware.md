# JamBox Hardware (v2: hardwired, all-in-one)

> **Decided 2026-11-24.** The choices here match the decision log in [enclosure.md](enclosure.md):
> Jam Radio, Pi 4 4 GB, Amp4, PC83-4, NeoMatrix 8×8, NFC-only presence, wall power, hardwood cartridges.
> Estimated total with those picks: **≈ $820** (electronics ≈ $460, enclosure, tools and cartridges ≈ $360).
> **Carts built 2026-11-24 with real prices: ≈ $950 all-in** (≈ $745 in carts incl. known shipping, plus
> finish, maple, grille sheet and tools still to buy). The Pi, Amp4 and SD card cost more than estimated. See
> the Results section of [shopping.md](shopping.md).

This replaces the v1 prototype list (Pi 3 B+ plus a Bluetooth speaker). v2 is a self-contained
box with built-in speakers, physical controls, an LED "face" that dances to the music,
and a slot that takes chunky **cartridges**. One USB-C charger powers everything.

- Shopping carts by store: [shopping.md](shopping.md).
- Enclosure design, the three design concepts, cartridge spec and build notes are in [enclosure.md](enclosure.md).
- Software changes this hardware needs are in [plans/2026-11-24-hardwired-v2.md](plans/2026-11-24-hardwired-v2.md).

---

## 1. Decisions at a glance

| Area | Choice | Why |
|---|---|---|
| Computer | **Raspberry Pi 4 Model B (4GB)** | It runs the whole stack (FastAPI, Next.js, librespot) with headroom. It runs cooler than a Pi 5 inside a closed wooden box. It's powered fine from the amp board. It works with the `rpi_ws281x` LED library. Raspberry Pi commits to producing it until at least **January 2034**. |
| Audio | **HiFiBerry Amp4** I2S amp HAT + 2× **Dayton Audio PC83-4** 3" full-range drivers | Clean digital audio with no headphone-jack hiss. Up to 2×30 W, far more than needed, so it loafs at toddler volumes. It also **powers the Pi from the same 12–20 V input**. |
| Power in | Panel-mount **USB-C** → **USB-PD trigger board set to 15 V** → Amp4 + 5 V buck for the LEDs | A single USB-C port that accepts any **45 W+ USB-C PD charger** (or PD power bank). 15 V/3 A = 45 W of headroom. |
| On/off + "it's on" light | Illuminated **latching anti-vandal pushbutton** on the 15 V rail | The steel button is toddler-proof, and its LED ring is the on/off indicator. Pairs with a read-only OS so a hard power-off can't corrupt the SD card. |
| NFC | **PN532** (Adafruit #364), kept from v1 | The existing code already uses it. The tuned antenna reads 30–40 mm tags through a thin wall easily. |
| Cartridge presence | **NFC-only** (pause after 2–3 missed polls) plus a click detent for feel. The microswitch is an optional add-on | NFC alone can detect removal (~1–1.5 s) with no extra part. Add the switch only if the slot mock-up test shows laggy or false pauses |
| Controls | 3× 30 mm arcade buttons (Back / Play-Pause / Skip) + rotary encoder volume knob | Arcade buttons are built for abuse. An encoder (not a pot) lets software enforce a max volume. |
| LEDs | 8×8 **WS2812B** NeoPixel matrix behind a diffuser, driven over SPI | Audio-reactive visualizer, boot/idle animations, volume bar and status. SPI avoids clashing with I2S audio. |
| Storage | 64 GB **high-endurance** microSD + read-only root filesystem (overlayfs) | Survives being unplugged mid-song. |

### Why not the alternatives?

| Option | Verdict |
|---|---|
| Pi 3 B+ (v1) | It works, but it has 1 GB RAM and an older Wi-Fi radio, and it's slower to build and run Next.js. Fine to reuse for bench testing. |
| Pi 5 | It's faster and has a built-in power button, but runs hotter (needs a fan in a closed box) and wants a 5 V/5 A PD supply. Its LED library support (`rpi_ws281x`) is not equivalent. Overkill here. |
| Pi Zero 2 W | Only 512 MB RAM, which is too tight for Next.js + FastAPI + librespot. There are also reports of audio stutter under load. |
| ESP32 + Spotify Connect (cspot) | Cheap and instant-on, but it can't host the web app and database, so it breaks the "device does everything" requirement. |
| Pi headphone jack + powered speakers | Hissy audio, plus a second power brick. That defeats the point of all-in-one. |
| Adafruit I2S 3 W Speaker Bonnet / HiFiBerry MiniAmp | Both are good, simpler amps powered from the Pi's 5 V. But then the whole box hangs off a 5 V/3 A USB-C budget, and LEDs + Pi + amp peaks exceed it. The Amp4 + 15 V PD design has real headroom. Keep the Bonnet as the budget fallback. |
| PN5180 reader | Its big range advantage only applies to ISO 15693 tags. With NTAG215 (ISO 14443A) it's no better than the PN532, and its Python support on the Pi is thin. |
| RC522 reader | Cheaper, but a smaller antenna and flakier through a wall. The PN532 is already proven in this codebase. |

---

## 2. Parts list

Items marked **†** were confirmed from the vendor's own listing on 2026-11-24, when the carts in
[shopping.md](shopping.md) were built; the rest are estimates. **Check stock and price before ordering.**

### Electronics

| # | Item | Specific part | Qty | ≈ Each | Where to buy | Notes |
|---|---|---|---|---|---|---|
| E1 | Single-board computer | Raspberry Pi 4 Model B, 4 GB | 1 | $100 † | [PiShop.us](https://www.pishop.us), [Adafruit](https://www.adafruit.com), [CanaKit](https://www.canakit.com), Micro Center | 2 GB also works; 4 GB gives headroom for Next.js builds. Nov 2026: $100 at PiShop and CanaKit, $120 Adafruit, $99.99 Micro Center (in-store only) |
| E2 | Amplifier HAT | HiFiBerry **Amp4** | 1 | $98.45 † | [hifiberry.com](https://www.hifiberry.com/shop/boards/hifiberry-amp4/), [PiShop](https://www.pishop.us) | 12–20 V input (4 Ω speakers); powers the Pi. Uses GPIO 2/3 (I2C), 4 (mute), 18–21 (I2S). $98.45 at PiShop; hifiberry.com is $64.90 + $38 FedEx from Switzerland (+ duties) |
| E3 | Speaker drivers | Dayton Audio **PC83-4** 3" full-range, 4 Ω | 2 | $15.49 † | [Parts Express 295-154](https://www.parts-express.com/Dayton-Audio-PC83-4-3-Full-Range-Poly-Cone-Driver-295-154) | 30 W RMS, 86.8 dB. Upgrade: Dayton RS75-4 (~$30 †) |
| E4 | NFC reader | Adafruit **PN532** breakout v1.6 (#364) | 1 | $39.95 † | [Adafruit](https://www.adafruit.com/product/364) | **Out of stock Nov 2026.** Bought the V3 alt instead: HiLetgo PN532 V3 ($8.99 †, Amazon B01I1J17LC; no Elechouse-brand listing on Amazon) |
| E5 | USB-PD trigger | Adafruit **HUSB238** PD Dummy Breakout (#5807) | 1 | $5.95 † | [Adafruit](https://www.adafruit.com/product/5807) | Bridge the **15 V** jumper. Up to 3.25 A |
| E6 | USB-C panel mount | Panel-mount USB-C female → USB-C male extension, 20–30 cm, rated 5 A/100 W | 1 | $9.95 † | Adafruit #4218, Amazon | The only port Jamie will see. Mount it in a recessed pocket on the back. #4218 fits a 21.5–27 mm hole in panels ≤16 mm; its listing gives no current/PD rating, so confirm 15 V/3 A passes before relying on it |
| E7 | 5 V supply for LEDs | Pololu **D36V28F5** 5 V 3.2 A step-down regulator | 1 | $16.99 † | [Pololu](https://www.pololu.com), Amazon (GetFPV) | 15 V → 5 V for the LED matrix and the level shifter. Nov 2026: Pololu $23.95 out of stock, RobotShop $21.95 restocking, Amazon/GetFPV $16.99 + $4.99 ship |
| E8 | Power switch + light | 19 mm **latching** illuminated anti-vandal stainless pushbutton, ≥3 A, 12 V LED ring | 1 | $13.49 † | Amazon (APIELE 10 A, B07V96FYHP) | Switches the 15 V rail. Wire the ring LED through it so it lights when ON |
| E9 | Buttons | 30 mm arcade buttons (Sanwa OBSF-30 or Adafruit 30 mm) | 3 | $2.50 † | [Adafruit](https://www.adafruit.com), Paradise Arcade Shop, Amazon | Pick three colors: Back, Play/Pause, Skip. Adafruit LED versions #3490/#3487/#3488 (blue, green, yellow; no orange) |
| E10 | Volume encoder | Bourns **PEC11R-4220F-S0024** (24 detents, push switch) | 1 | $2.34 † | Mouser 652-PEC11R-4220F-S24, DigiKey | Or Adafruit rotary encoder #377 (out of stock Nov 2026) |
| E11 | Volume knob | 40–50 mm knob with a 6 mm shaft (wood, or 3D printed) | 1 | $11.99 † | Amazon (B099DHHGGQ, 44 × 25 mm aluminium, set screw) | Big and grippy. Grub-screw or D-shaft fit, glued. The Amazon knob is the backup; print or turn one if you prefer. Counterbore the top panel under the encoder (see enclosure.md) so enough shaft sticks out |
| E12 | LED matrix | Adafruit NeoPixel **NeoMatrix 8×8** (#1487), or a flexible 8×8/16×16 WS2812B panel | 1 | $34.95 † | Adafruit, BTF-Lighting (Amazon) | Software-capped at ~20% brightness |
| E13 | Level shifter | **74AHCT125** quad level shifter (Adafruit #1787) | 1 | $1.50 † | Adafruit | 3.3 V GPIO → 5 V NeoPixel data |
| E14 | Slot sensor (**optional**, pending test) | Omron **D2F-01L3** roller-lever microswitch (or SS-5GL) | 1 | ~$3 | DigiKey, Mouser | Only if NFC-only removal is laggy or flaky. Alt: Adafruit IR break-beam 3 mm (#2167) |
| E15 | GPIO breakout | 2×20 **extra-tall stacking header** (Adafruit #1979) + screw-terminal or Perma-Proto HAT | 1 | $2.95 † + HAT | Adafruit | The Amp4 sits on the Pi; this exposes free pins for wiring |
| E16 | Storage | SanDisk **High Endurance** 64 GB microSD | 1 | $30.95 † | PiShop, Amazon, B&H | High-endurance cards are made for constant writes. Amazon's $25.99 listing has a 2-card minimum |
| E17 | Pi cooling | Aluminum heatsink set for Pi 4 | 1 | $2.95 † | PiShop add-on, Amazon | Passive. The box has vent holes (see enclosure.md) |
| E18 | NFC tags | **NTAG215 30–35 mm** round stickers or PVC coins | 25–60 | $0.32 † | [ShopNFC](https://www.shopnfc.com), [Seritag](https://seritag.com), Amazon | Bigger tags read farther. Avoid "on-metal" tags (not needed). Nov 2026: neither ShopNFC nor Seritag stocks NTAG215; Amazon 30 mm coins 30-pack $9.50 (genuine NXP not stated). Seritag genuine-NXP NTAG213 29 mm is $0.37 |
| E19 | Charger | Any **USB-C PD charger, 45 W+, with a 15 V profile** (most 45–65 W GaN chargers) | 1 | $22.49 † | Anker, UGREEN, Apple, etc. | Check that the label lists 15 V ⎓ 3 A. UGREEN Nexode 65W (B091BGMKYS) lists 15V/3A |
| E20 | Wiring kit | 18 AWG speaker wire, 22 AWG silicone hookup wire, JST-XH connector kit + crimper, heat-shrink, inline 3 A blade fuse holder | 1 | $53 † | Amazon | Use keyed connectors (JST-XH) everywhere, not loose Dupont jumpers |
| E21 | Mounting | M2.5 nylon standoff kit, M3 brass threaded inserts | 1 | $19 † | Amazon | Keep brass/steel **≥30 mm away** from the NFC antenna |

**Electronics subtotal: about $494** at Nov 2026 cart prices, including the charger and 60 tags (estimate was $450–520).

### Enclosure and finishing

The full rationale and cut list are in [enclosure.md](enclosure.md).

| Item | Spec | ≈ Cost | Where |
|---|---|---|---|
| Baltic birch plywood | 12 mm (½") and 6 mm (¼"), void-free, about one 30"×60" panel of each | $100 † (Woodcraft 30×30": 2× ½" at $38.99, 1× ¼" at $21.99) | Woodcraft (Grand Rapids store), Rockler, local hardwood dealer. Not Home Depot: its birch panels aren't Baltic birch |
| Hardwood for cartridges | Maple or cherry, ¾" (19 mm) and ½" (12 mm) boards, about 4 bd-ft | $30–50 | Woodcraft of Grand Rapids, local hardwood dealer |
| Speaker grille mesh | Perforated steel or aluminum sheet, ~2 mm holes, or a 3" steel grille insert | $18–55 | Amazon 12×12" perforated stainless (~$18). Not bought yet: Parts Express has no sheet (its 3" grille fits 2.5" drivers) and McMaster's smallest is 24×24" from $54 |
| Grille cloth + polyfill | Acoustic grille cloth, polyester fiberfill for the speaker chambers | $26 † | Parts Express |
| LED diffuser | 3 mm opal/frosted acrylic, or 0.6 mm (1/42") maple veneer | $10 | TAP Plastics, Amazon |
| Fasteners | **Tamper-resistant Torx (pin-in T20)** screws + matching bit, M3/#6 threaded inserts | $20 † | McMaster-Carr (91900A848 + 7233A61), Amazon. M3 pin-in Torx takes a **T8** bit, not T20 |
| Feet | 4× rubber feet, ~10 mm tall (lifts the box for bottom vents) | $10 † | Amazon, hardware store |
| Glue | Titebond III | $9.99 † | Anywhere |
| Finish | Water-based, **toy-safe finish labeled EN 71-3 / ASTM F963**, plus non-toxic paint for accents | $25–40 | Woodcraft, Rockler |
| Router bits | 6 mm (¼") roundover, 45° chamfer, rabbeting set | $40–60 | Rockler, Amazon (if not owned) |
| Hole cutting | 75 mm (3") hole saw for the drivers, 32–35 mm Forstner (tag pockets), 6 mm brad-point (grille holes), 30 mm Forstner or step bit (buttons) | $40 | Rockler, Amazon |

**Enclosure subtotal: about $250–350**, depending on tools you already own.

### Optional

| Item | ≈ Cost | Notes |
|---|---|---|
| 3D printer | $0 | **You already have an Ender 3 Pro.** See "3D printer decision" in enclosure.md |
| UL 2056-certified USB-C PD power bank, 20,000 mAh+, with **15 V output** | $50–80 | **Deferred: v1 is wall-powered.** For later portable use; see "Battery spike" in enclosure.md. No battery goes *inside* the box |
| Spare Pi 4 + SD card | $70 | Swap in a backup if something dies |

**Overall: about $860–950** at Nov 2026 prices (the high end includes router bits and hole cutters), inside the original <$1000 budget.

---

## 3. Power architecture

```
 Wall ── USB-C PD charger (45 W+, 15 V profile)
            │  USB-C cable
            ▼
   [E6] Panel-mount USB-C (back of box, recessed)
            │
   [E5] HUSB238 PD trigger ── requests 15 V
            │ 15 V
          [fuse 3 A]
            │
   [E8] Latching illuminated power button ──(ring LED = "ON" light)
            │ 15 V
     ┌──────┴───────────────┐
     ▼                      ▼
 [E2] HiFiBerry Amp4    [E7] Pololu 5 V buck
  │ powers Pi via 40-pin  │ 5 V
  ▼                       ├─► NeoPixel 8×8 matrix (+ 1000 µF cap)
 [E1] Raspberry Pi 4       └─► 74AHCT125 level shifter VCC
  (PN532, buttons, encoder and slot switch run from the Pi's 3.3 V)
```

**Power budget (worst case):** Pi 4 under load ≈ 6 W, Amp4 at loud volume ≈ 10 W,
LED matrix at 20% brightness ≈ 2.5 W. Total ≈ 19 W against 45 W available.
Typical playback is 6–9 W.

> Note: if the charger can't supply 15 V, the HUSB238 falls back to 5 V and the Amp4 won't start.
> The power-button light will be on but nothing boots. Use a 45 W+ PD charger.

---

## 4. GPIO pin map (Pi 4 + Amp4)

| Function | GPIO | Physical pin | Notes |
|---|---|---|---|
| I2C SDA (Amp4 config **and** PN532) | 2 | 3 | Shared bus. PN532 is at 0x24; confirm no clash with `i2cdetect -y 1` |
| I2C SCL | 3 | 5 | Shared |
| Amp4 MUTE | 4 | 7 | **Reserved by Amp4. Do not use** |
| I2S BCLK / LRCLK / DIN / DOUT | 18, 19, 20, 21 | 12, 35, 38, 40 | **Reserved by Amp4** |
| LED matrix data (SPI0 MOSI) | 10 | 19 | Through the 74AHCT125 → 330 Ω → matrix DIN. SPI avoids the PWM/PCM clash with I2S |
| Encoder A | 17 | 11 | Internal pull-up |
| Encoder B | 27 | 13 | Internal pull-up |
| Encoder push (mute toggle) | 22 | 15 | Optional |
| Button: Back | 23 | 16 | To GND, internal pull-up |
| Button: Play/Pause | 24 | 18 | To GND, internal pull-up |
| Button: Skip | 25 | 22 | To GND, internal pull-up |
| Slot microswitch (NO contact) | 5 | 29 | To GND, internal pull-up; closed = cartridge present |
| PN532 3.3 V / GND | – | 1 / 6 | As in v1 |
| Spare | 6, 12, 13, 16, 26 | 31, 32, 33, 36, 37 | 12/13 are PWM: keep free for future button LEDs |

**Do not use GPIO 18 (PWM) for the LEDs.** It's the I2S clock, so audio and LEDs would fight over it.
On a Pi 4 the SPI method needs a fixed core clock. Add this to `/boot/firmware/config.txt`:

```
dtparam=i2c_arm=on
dtparam=spi=on
core_freq=500
core_freq_min=500
```

The HiFiBerry overlay is normally auto-detected from the HAT's EEPROM. If not, add the
overlay named in HiFiBerry's Amp4 documentation. Remove `dtparam=audio=on` so the onboard
audio isn't selected.

### Wiring summary

```
 Pi 4 ─[stacking header]─ Amp4 ─[speaker terminals]─ L / R drivers (18 AWG, twisted pair)
   │
   ├─ pin 1 (3.3V), 3 (SDA), 5 (SCL), 6 (GND) ──────── PN532 (I2C mode*)
   ├─ pin 19 (GPIO10) ─ 74AHCT125 (5 V) ─ 330 Ω ────── NeoPixel DIN
   ├─ pins 11/13/15 + GND ──────────────────────────── Rotary encoder A/B/push
   ├─ pins 16/18/22 + GND ──────────────────────────── Arcade buttons Back/Play/Skip
   └─ pin 29 + GND ─────────────────────────────────── Slot microswitch (NO)

 5 V buck ─ + ─ 1000 µF cap ─ NeoPixel 5V;  GND common with Pi GND
```

\* I2C mode: on the Elechouse V3 set DIP SW1 = ON, SW2 = OFF. On the Adafruit #364 set the
SEL0/SEL1 jumpers for I2C as shown in Adafruit's PN532 guide.

Wire everything to the Pi through **JST-XH connectors** so the electronics sled can be
unplugged and slid out without tools.

---

## 5. NFC through wood: what matters

Wood **density barely matters** at 13.56 MHz. The reader couples to the tag through a
magnetic field, and dry wood and plastic are almost transparent to it. What *does* matter:

1. **Distance.** The total gap between antenna and tag (wall + clearance + depth of the tag
   inside the cartridge) is what counts. Adafruit quotes up to ~10 cm for a credit-card-sized
   tag and ~5 cm for a small fob. **Design target: ≤ 20 mm gap**, which leaves a large margin.
2. **Tag size.** Bigger tag antenna = more range. Use 30–35 mm round tags, not 20–25 mm.
3. **Orientation.** Keep the tag face **parallel** to the reader's antenna.
4. **Metal.** Screws, threaded inserts, foil tape, metallic paint and the speaker magnets
   detune the antenna. Keep all metal **≥ 30 mm** from the antenna, and put the speakers on the
   far side of the box.
5. **Moisture.** Very wet wood absorbs a little energy. Sealed, finished, kiln-dried wood is fine.

**Bench test before gluing anything:** mount the PN532 behind a 6 mm offcut of the
real plywood. Then hold a sample cartridge at the real slot position and confirm it reads
in both orientations, 20 times in a row.

---

## 6. Raspberry Pi setup (v2)

1. Flash **Raspberry Pi OS Lite (64-bit)** with Raspberry Pi Imager. Set the hostname
   `jambox`, enable SSH and configure Wi-Fi.
2. `sudo apt update && sudo apt full-upgrade -y`
3. Enable I2C and SPI: `sudo raspi-config` → Interface Options. Add the `config.txt` lines from §4.
4. Reboot, then confirm the Amp4 is the sound card with `aplay -l`. Check I2C devices with `i2cdetect -y 1`.
5. Install the app: `./scripts/pi-setup.sh`. Note: it still contains the v1 Bluetooth steps, which are
   being replaced. See the [v2 plan](plans/2026-11-24-hardwired-v2.md).
6. Once everything works: `sudo raspi-config` → Performance → **Overlay file system → enable**
   so the root filesystem is read-only. Keep the SQLite database on a small writable partition
   (see the v2 plan).

> Bluetooth pairing steps from v1 are no longer needed.
