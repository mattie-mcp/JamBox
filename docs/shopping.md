# JamBox v2 shopping brief

The decided parts from [hardware.md](hardware.md) and [enclosure.md](enclosure.md), grouped into **one cart per
store** to keep shipping down. This is the working list for building carts and comparing prices in Chrome.

**Rules for whoever (or whatever) builds the carts:**
- **Add to cart only. Never check out, pay, or enter payment or address details.** The person reviews and buys.
- Record for each line: exact product title, part number, unit price, qty, in-stock (Y/N), and the page URL.
  Record each cart's subtotal, shipping estimate, and the free-shipping threshold if shown.
- If an item is out of stock, note it and add the listed alternate. Don't substitute anything else without asking.
- Stop and ask if a site needs a login, a CAPTCHA, or a dialog appears.
- Write the results into the "Results" table at the bottom of this file.

---

## Cart 1: PiShop.us (or Adafruit). Pi + amp

| Item | Part | Qty | Est. | Alternate |
|---|---|---|---|---|
| Raspberry Pi 4 Model B, **4 GB** | RPi 4B 4GB | 1 | $55–65 | Adafruit, CanaKit, Micro Center |
| HiFiBerry **Amp4** | Amp4 (not Amp4 Pro) | 1 | $64.90 | hifiberry.com direct |
| Aluminium heatsink set for Pi 4 | – | 1 | ~$6 | Amazon |

**Compare:** Pi 4 4 GB across PiShop, Adafruit, CanaKit and Micro Center (prices moved in 2025–26). For the
Amp4, PiShop vs hifiberry.com, *including shipping*.

## Cart 2: Adafruit. NFC, power and controls

| Item | Part | Qty | Est. |
|---|---|---|---|
| PN532 NFC/RFID breakout v1.6 | #364 | 1 | $39.95 |
| USB-C PD Dummy Breakout, HUSB238 (I2C or Fixed) | #5807 | 1 | ~$6 |
| NeoPixel NeoMatrix 8×8 | #1487 | 1 | ~$35 |
| 74AHCT125 quad level shifter | #1787 | 1 | ~$2 |
| GPIO stacking header, 2×20 extra-tall | #1979 | 1 | ~$2.50 |
| 30 mm arcade buttons, 3 colours (blue, green, orange or nearest) | search "Arcade Button 30mm" | 3 | ~$2–3 ea |
| Panel-mount USB-C female → USB-C male extension cable | search "Panel Mount USB C" | 1 | ~$6–10 |
| Rotary encoder with push switch (if not buying Bourns at DigiKey) | #377 | 1 | ~$4.50 |
| 19 mm latching illuminated anti-vandal pushbutton, if Adafruit has one rated ≥ 3 A at 12–15 V | search "Rugged Metal Pushbutton latching" | 1 | ~$8–15 |

**Compare:** the PN532 (#364, $39.95) vs the Elechouse PN532 V3 (~$15, Amazon). The code works with both. Adafruit's is
the better-documented board. Check the free-shipping threshold; Cart 2 may cross it.

## Cart 3: Parts Express. Speakers and grilles

| Item | Part | Qty | Est. |
|---|---|---|---|
| Dayton Audio PC83-4 3" full-range | 295-154 | 2 | $15.49 ea |
| Acoustic grille cloth (black or natural) | – | 1 | ~$8 |
| Polyester fiberfill (speaker stuffing) | – | 1 | ~$5 |
| Perforated metal grille sheet, ~2 mm holes, steel or aluminium | – | 1 | ~$10–15 |

## Cart 4: Pololu. 5 V regulator

| Item | Part | Qty | Est. |
|---|---|---|---|
| 5 V 3.2 A step-down regulator | **D36V28F5** | 1 | ~$15 |

**Compare:** Pololu direct vs RobotShop, DigiKey or Amazon resellers, *with shipping*. A single cheap part may be better bundled elsewhere.

## Cart 5: DigiKey (or Mouser). Small electronics

| Item | Part | Qty | Est. |
|---|---|---|---|
| Bourns rotary encoder, 24 detents, push switch | PEC11R-4220F-S0024 | 1 | ~$3 |
| 19 mm latching illuminated anti-vandal pushbutton, ≥ 3 A, 12 V LED ring (if not at Adafruit) | – | 1 | ~$10–15 |
| 3 A inline blade fuse holder + 3 A fuses | – | 1 | ~$5 |
| *(optional, only if the slot test fails)* Omron roller-lever microswitch | D2F-01L3 | 1 | ~$3 |

## Cart 6: Amazon. Consumables

| Item | Qty | Est. | Notes |
|---|---|---|---|
| SanDisk **High Endurance** microSD, 64 GB | 1 | ~$15 | Not "Ultra" |
| **NTAG215** round tags, **30–35 mm**, 50 pack (wet inlay, PET stickers or PVC coins) | 1 | ~$15–30 | Compare with ShopNFC / Seritag |
| USB-C PD charger, **45 W+, label must list 15 V ⎓ 3 A** (Anker, UGREEN) | 1 | ~$25–40 | |
| JST-XH connector kit + crimper | 1 | ~$30 | |
| 22 AWG silicone hookup wire kit; 18 AWG speaker wire | 1 each | ~$20 | |
| M2.5 nylon standoff kit; M3 brass heat-set/threaded inserts | 1 each | ~$15 | |
| Rubber feet, ~10 mm tall | 4 | ~$8 | |
| **Ender 3 Pro:** textured PEI spring-steel sheet, 235 × 235 mm | 1 | ~$20 | For PETG |
| PETG filament, 1 kg (pick a toy-friendly colour) + PLA for test prints | 1–2 | ~$20 ea | |

**Compare:** NTAG215 30–35 mm tags at ShopNFC, Seritag and Amazon (price per tag; check it's genuine NXP NTAG215).

## Cart 7: McMaster-Carr. Hardware

| Item | Qty | Est. | Notes |
|---|---|---|---|
| Tamper-resistant Torx (pin-in T20) wood or machine screws to match the inserts + matching bit | 1 pack | ~$15 | |
| HDPE sheet, ~6 mm (¼"), at least 12 × 12" (slot insert) | 1 | ~$15 | Or a plain HDPE cutting board |

## Cart 8: Rockler or Woodcraft (or a local lumber yard). Wood and finishing

| Item | Qty | Est. | Notes |
|---|---|---|---|
| Baltic birch plywood, **12 mm (½")**, 24 × 30" or larger project panel | 1–2 | $30–50 | |
| Baltic birch plywood, **6 mm (¼")**, 24 × 30" | 1 | $15–25 | |
| Maple (or cherry) board, ¾" and ½" thick, ~3–4 bd-ft total (cartridges, handle uprights) | – | $30–50 | |
| Hardwood dowel, **1" (25 mm)** × 36" (handle) | 1 | ~$8 | |
| Titebond III | 1 | ~$10 | |
| Water-based toy-safe finish (labelled EN 71-3 / ASTM F963) | 1 | ~$25 | |
| Router bits: ¼" and ⅜" roundover, 45° chamfer (if not owned) | – | $40–60 | |
| 3" hole saw (driver cutouts), 1-⅜" (35 mm) Forstner (tag pockets), 6 mm brad-point bit (grille holes) | – | ~$40 | |

---

## Results

*(Filled in when the carts are built.)*

| Cart | Store | Items in stock | Subtotal | Shipping | Free-ship threshold | Notes |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
