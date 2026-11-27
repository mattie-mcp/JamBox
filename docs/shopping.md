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

> **Current state (2026-11-27):** the per-store lists below are the original brief. The **Results** section is what is
> actually in each cart after the design fixes and the cost-review savings.

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
| NeoPixel Shield 5×8 (portrait; replaced the NeoMatrix 8×8 #1487 on 11/27) | #1430 | 1 | $27.95 |
| 74AHCT125 quad level shifter | #1787 | 1 | ~$2 |
| GPIO stacking header, 2×20 extra-tall | #1979 | 1 | ~$2.50 |
| 24 mm mini LED arcade buttons, blue / green / yellow (switched from 30 mm on 11/27) | #3432 / #3433 / #3431 | 3 | $2.50 ea |
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
| Polyester fiberfill (speaker stuffing); use what you have | – | 0 | ~$0–5 |
| Perforated metal grille sheet, ~2 mm holes, steel or aluminium | – | 1 | ~$10–15 |

## Cart 4: Pololu. 5 V regulator (dropped: Adafruit MPM3610 #4739 instead)

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
| **NTAG215** round tags, **30–35 mm**, ~30 pack (wet inlay, PET stickers or PVC coins) | 1 | ~$15–30 | Compare with ShopNFC / Seritag |
| USB-C PD charger, **45 W+, label must list 15 V ⎓ 3 A** (Anker, UGREEN) | 1 | ~$25–40 | |
| JST-XH kit with **pre-crimped leads** (no crimper) | 1 | ~$8 | |
| 22 AWG silicone hookup wire kit (also for the speakers) | 1 | ~$16 | |
| M2.5 nylon standoff kit; M3 brass heat-set/threaded inserts | 1 each | ~$15 | |
| Rubber feet, ~10 mm tall, **screw-on** | 4 | ~$8 | |
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
| Baltic birch plywood, **12 mm (½")**, 30 × 30" | 1 | $30–50 | |
| Baltic birch plywood, **6 mm (¼")**, 24 × 30" | 1 | $15–25 | |
| Maple (or cherry) board, ¾" and ½" thick, ~3–4 bd-ft total (8/4 maple milled to 30 mm for the cartridges; sled rails) | – | $30–50 | |
| ~~Hardwood dowel, 1" × 36" (handle)~~ | 0 | – | Dropped 2026-11-27: no handle |
| Titebond III | 1 | ~$10 | |
| Water-based toy-safe finish (labelled EN 71-3 / ASTM F963) | 1 | ~$25 | |
| Router bits: ¼" and ⅜" roundover, 45° chamfer (if not owned) | – | $40–60 | |
| 1-⅜" (35 mm) Forstner (tag pockets), 15/16" (24 mm) Forstner (buttons), ⅞" Forstner (USB-C/switch counterbores), 6 mm brad-point (grille holes) | – | ~$40 | |
| Maple Shaker knob, 2", 2-pack (volume knob + spare) | 1 | ~$6 | |

---

## Results

Carts built in Chrome on **2026-11-24** (add to cart only; nothing bought). Prices are what each cart showed that
day; several are Black Friday sale prices. Shipping marked "at checkout" needs an address, which was not entered.

| Cart | Store | Items in stock | Subtotal | Shipping | Free-ship threshold | Notes |
|---|---|---|---|---|---|---|
| 1 | [PiShop.us](https://www.pishop.us/cart.php) | 3/3 | $232.35 | At checkout (USPS / FedEx) | None listed | SD card moved here from Amazon |
| 2 | [Adafruit](https://www.adafruit.com/shopping_cart) | 10 lines (MPM3610 buck added 11/27); buttons switched to 24 mm minis 11/27; 74AHCT125 #1787 out of stock (moved to Mouser); PN532 #364 and encoder #377 **out of stock** | $68.20 ($57.97 with code OhFudge15) | At checkout | $200 (US) | No 19 mm latching switch rated for 12–15 V |
| 3 | [Parts Express](https://www.parts-express.com/cart) | 2/2 | $40.96 | $9.95 | $99 | Polyfill removed 11/27 (use what you have). BLACKFRI15 (15% off $75+, ends 11/29) doesn't reach |
| 4 | Pololu | **0/1** (D36V28F5 out of stock, backorder only) | n/a | n/a | n/a | Dropped 11/27: Adafruit MPM3610 instead (Cart 2) |
| 5 | [Mouser](https://www.mouser.com/Cart/) (DigiKey showed a CAPTCHA) | 7/7 | $11.50 | $8.49 UPS Ground + $0.63 tariff | n/a | Switch and fuse moved to Amazon; level shifter and wiring passives added 11/27 |
| 6 | [Amazon](https://www.amazon.com/gp/cart/view.html) | 8 JamBox lines (9 units) | $91.03 | Free (Prime) | Prime | SanDisk card not added: 2-card minimum. PEI sheet, PETG and PLA moved to **Saved for later** on 11/27 (printing comes last). PN532 removed 11/27 (you already own the HiLetgo V3). UGREEN charger moved to **Saved for later** 11/27 (your own charger lists 15 V ⎓ 3 A). 11/27 savings: regulator, crimper kit, speaker wire, aluminium knob and one tag pack removed. Your Scotch tape is also in this cart |
| 7 | [McMaster-Carr](https://www.mcmaster.com/order/) | 3/3 | $30.36 | At checkout | n/a | Perforated sheet not added (24×24" minimum, $54+) |
| 8 | [Woodcraft](https://www.woodcraft.com/cart) | 4/4 | $76.96 | Free (over $50, through Dec 1) | $50 | Switched from Rockler (cart emptied). Woodcraft of Grand Rapids is local for maple and pickup. Finish and tools not added (see below) |
| | **hifiberry.com** | comparison only | $64.90 | $38.00 FedEx | | Amp4 left in that cart for comparison; **remove it, don't buy both** |

**In carts: $551.36 of merchandise plus $19.07 of known shipping ≈ $570** (≈ $560 with Adafruit's OhFudge15 code). PiShop, Adafruit and McMaster shipping (≈ $25)
and sales tax come on top.

### Line items

| Cart | Item (exact title) | Part / SKU | Unit | Qty | Stock | Link |
|---|---|---|---|---|---|---|
| 1 | Raspberry Pi 4 Model B/4GB | PiShop 4GB-9004 (SC0194) | $100.00 | 1 | In stock | [pishop](https://www.pishop.us/product/raspberry-pi-4-model-b-4gb/) |
| 1 | ↳ add-on: Aluminum Heatsink for Raspberry Pi 4B (3-Pack) | PiShop 1723 | $2.95 | 1 | In stock | same page |
| 1 | HiFiBerry AMP4 | PiShop 23-1 | $98.45 | 1 | In stock | [pishop](https://www.pishop.us/product/hifiberry-amp4/) |
| 1 | SanDisk High Endurance MicroSDXC Card - 64GB - Class10 - BLANK | SanDisk High Endurance 64GB | $30.95 | 1 | In stock | [pishop search](https://www.pishop.us/search.php?search_query=sandisk+high+endurance+64gb) |
| 2 | Adafruit USB Type C Power Delivery Dummy Breakout - I2C or Fixed - HUSB238 | #5807 | $5.95 | 1 | In stock | [adafruit](https://www.adafruit.com/product/5807) |
| 2 | Adafruit NeoPixel Shield for Arduino - 40 RGB LED Pixel Matrix (5×8) | #1430 | $27.95 | 1 | 33 in stock | [adafruit](https://www.adafruit.com/product/1430) |
| 5 | Texas Instruments SN74AHCT125N quad buffer, DIP-14 (same chip as Adafruit #1787, which went out of stock 11/27) | Mouser 595-SN74AHCT125N | $0.95 | 1 | 1,002 in stock | [mouser](https://www.mouser.com/c/?q=SN74AHCT125N) |
| 2 | Stacking Header - 2x20 Extra Tall Header | #1979 | $2.95 | 1 | In stock | [adafruit](https://www.adafruit.com/product/1979) |
| 2 | Mini LED Arcade Button - 24mm Translucent Blue / Green / Translucent Yellow (Back / Play-Pause / Skip) | #3432 / #3433 / #3431 | $2.50 | 1 each | In stock | [adafruit](https://www.adafruit.com/product/3432) |
| 2 | Male DC Power adapter - 2.1mm plug to screw terminal block (15 V into the Amp4 jack; confirm the jack is 5.5 × 2.1 mm) | #369 | $2.00 | 1 | In stock | [adafruit](https://www.adafruit.com/product/369) |
| 2 | MPM3610 5V Buck Converter Breakout - 21V In 5V Out at 1.2A (LED 5 V; replaces the Pololu) | #4739 | $6.95 | 1 | In stock | [adafruit](https://www.adafruit.com/product/4739) |
| 2 | Multi-Colored Heat Shrink Pack - 3/32" + 1/8" + 3/16" Diameters | #1649 | $4.95 | 1 | In stock | [adafruit](https://www.adafruit.com/product/1649) |
| 2 | USB C Round Panel Mount Extension Cable | #4218 | $9.95 | 1 | In stock | [adafruit](https://www.adafruit.com/product/4218) |
| 3 | Dayton Audio PC83-4 3" Full-Range Poly Cone Driver | 295-154 | $15.49 | 2 | 1,074 in stock | [parts-express](https://www.parts-express.com/Dayton-Audio-PC83-4-3-Full-Range-Poly-Cone-Driver-295-154) |
| 3 | Parts Express Speaker Grille Cloth Black Yard 70" Wide | 260-335 | $9.98 | 1 | In stock | [search](https://www.parts-express.com/search?keywords=260-335) |
| 5 | Bourns PEC11R-4220F-S0024 Encoders 20mm SHAFT w/SWITCH | Mouser 652-PEC11R-4220F-S24 | $2.34 | 1 | 8,085 in stock | [mouser](https://www.mouser.com/ProductDetail/Bourns/PEC11R-4220F-S0024) |
| 5 | Adafruit Perma-Proto HAT for Pi Mini Kit - No EEPROM (the permanent GPIO breakout; out of stock at Adafruit) | Mouser 485-2310 | $4.95 | 1 | 91 in stock | [mouser](https://www.mouser.com/c/?q=485-2310) |
| 5 | Panasonic EEU-FR1C102 1000 µF 16 V electrolytic (across 5 V at the LED shield) | Mouser 667-EEU-FR1C102 | $0.98 | 1 | 1,550 in stock | [mouser](https://www.mouser.com/c/?q=EEU-FR1C102) |
| 5 | YAGEO CFR-25JB-52-330R, 330 Ω ¼ W (LED data line + spare) | Mouser 603-CFR-25JB-52-330R | $0.11 | 2 | 7,270 in stock | [mouser](https://www.mouser.com/c/?q=CFR-25JB-52-330R) |
| 5 | YAGEO CFR-25JB-52-470R, 470 Ω ¼ W (power-switch ring LED at 15 V + spare) | Mouser 603-CFR-25JB-52-470R | $0.11 | 2 | In stock | [mouser](https://www.mouser.com/c/?q=CFR-25JB-52-470R) |
| 5 | KEMET C320C104K5R5TA 0.1 µF 50 V ceramic (level-shifter decoupling + spare) | Mouser 80-C320C104K5R5TA | $0.92 | 2 | In stock | [mouser](https://www.mouser.com/c/?q=C320C104K5R5TA) |
| 6 | 30pcs NFC Tags NTAG215 NFC Coins Rewritable White NFC Tag Round 30mm (two per cartridge) | B07PFC2FH5 | $9.50 | 2 | In stock | [amazon](https://www.amazon.com/dp/B07PFC2FH5) |
| 6 (saved for later) | UGREEN Nexode 65W USB C Charger Block, 3-Port (lists 15V/3A); backup only, you own a 15 V ⎓ 3 A charger | B091BGMKYS | $22.49 | 1 | In stock | [amazon](https://www.amazon.com/dp/B091BGMKYS) |
| 6 | APIELE 10 Amp 19mm Latching Push Button Switch 12V SPST LED (stainless, blue ring) | B07V96FYHP | $13.49 | 1 | In stock | [amazon](https://www.amazon.com/dp/B07V96FYHP) |
| 6 | 2pcs 18AWG Inline Fuse Holder with 3A Mini Fuse | B0DC3LVV75 | $5.59 | 1 | In stock | [amazon](https://www.amazon.com/dp/B0DC3LVV75) |
| 6 | XH 2.54mm Connector Socket Kit and Pre-Crimped Cable Wire 2–7 Pin (90 × 13 cm 22 AWG leads, heat-shrink; no crimper) | B0CJ6JDMJH | $7.99 | 1 | In stock | [amazon](https://www.amazon.com/dp/B0CJ6JDMJH) |
| 6 | TUOFENG 22 AWG Silicone Wire Kit, 6 Colors, 26.3 ft Each | B07G2JWYDW | $15.99 | 1 | In stock | [amazon](https://www.amazon.com/dp/B07G2JWYDW) |
| 6 | 365 Pcs M2.5 Black Nylon Hex Standoff Screw Nut Kit | B0FPMC9917 | $9.99 | 1 | In stock | [amazon](https://www.amazon.com/dp/B0FPMC9917) |
| 6 | HANGLIFE Heat-Set Threaded Inserts, M3 x D5 x L4 (100 pcs) | B0CS6VZYL8 | $8.99 | 1 | In stock | [amazon](https://www.amazon.com/dp/B0CS6VZYL8) |
| 6 | smseace 100PCS (5 Sizes) Rubber Feet with Washer and Screws | B08PBH875X | $9.99 | 1 | In stock | [amazon](https://www.amazon.com/dp/B08PBH875X) |
| 6 (saved for later) | PEI Flexi Steel Magnetic Build Plate 235×235 (Ender 3 Pro; includes magnetic base) | B09WZSGXFL | $15.99 | 1 | In stock | [amazon](https://www.amazon.com/dp/B09WZSGXFL) |
| 6 (saved for later) | SUNLU PETG Filament 1.75mm, 1kg, Black | B0DJS3PJVX | $11.96 | 1 | In stock | [amazon](https://www.amazon.com/dp/B0DJS3PJVX) |
| 6 (saved for later) | SUNLU PLA 3D Printer Filament, Black, 1KG | B07XG3RM58 | $11.19 | 1 | In stock | [amazon](https://www.amazon.com/dp/B07XG3RM58) |
| 7 | Tamper-Resistant Torx 18-8 SS Button Head Screws, M3 x 0.5 x 10 mm (pack of 50) | 91900A848 | $12.54 | 1 | Delivers tomorrow | [mcmaster](https://www.mcmaster.com/91900A848/) |
| 7 | Tamper-Resistant Torx Bit, 1/4" Hex Shank, T8 | 7233A61 | $7.84 | 1 | Delivers tomorrow | [mcmaster](https://www.mcmaster.com/7233A61/) |
| 7 | Moisture-Resistant HDPE Sheet 12" x 12" x 1/4" (FDA) | 8619K461 | $9.98 | 1 | Delivers tomorrow | [mcmaster](https://www.mcmaster.com/8619K461/) |
| 8 | Woodcraft Woodshop Baltic Birch Plywood, 1/2" x 30" x 30" (all 12 mm Radio parts fit on one) | Woodcraft #191388 | $38.99 | 1 | In stock online | [woodcraft](https://www.woodcraft.com/products/woodcraft-woodshop-baltic-birch-plywood) |
| 8 | Woodcraft Woodshop Baltic Birch Plywood, 1/4" x 30" x 30" | Woodcraft #191387 | $21.99 | 1 | In stock online | same page |
| 8 | Titebond III Ultimate Wood Glue - Waterproof, 16-oz | Woodcraft #145562 | $9.99 | 1 | In stock online | [woodcraft](https://www.woodcraft.com/products/titebond-iii-ultimate-wood-glue-waterproof) |
| 8 | Cindoco Shaker Knob - Maple - 2" Diameter - 3/4" Tenon - 2 Piece (volume knob + spare) | Woodcraft #161868 | $5.99 | 1 | Ships ~Dec 4 | [woodcraft](https://www.woodcraft.com/products/cindoco-shaker-knob-maple-2-diameter-3-4-tenon-2-piece) |

### Comparisons

| Item | Options (Nov 24, 2026) | Recommended |
|---|---|---|
| Pi 4 4 GB | PiShop **$100**, CanaKit $100, Micro Center $99.99 (in-store pickup only), Adafruit $120 | **PiShop**: same price as CanaKit, ships with the Amp4 and SD card |
| HiFiBerry Amp4 | PiShop **$98.45**, in stock, ships with the Pi. hifiberry.com $64.90 + $38.00 FedEx Intl Economy = **$102.90**, plus possible US duties, 1–6 weeks | **PiShop** |
| PN532 | Adafruit #364 $39.95, **out of stock**. Amazon V3 clones: HiLetgo $8.99 (220 reviews), AITRIP $7.99. No Elechouse-branded listing on Amazon | **HiLetgo V3** (in cart). Same PN532 chip and I2C, so the code works unchanged |
| NTAG215, 30–35 mm | **ShopNFC: no NTAG215** (stocks 210/213/216/DNA; e.g. NTAG213 Bullseye 38 mm €0.69). **Seritag: no NTAG215**; genuine-NXP NTAG213 29 mm **$0.37** (10–99). Amazon: 30 mm NTAG215 coins, 30-pack $9.50 = **$0.32/tag** (genuine NXP not stated); most Amazon 50-packs are 25 mm | **Amazon 30 mm coins** (2 packs = 60 tags, in cart: two per cartridge for 10 cartridges, plus spares). If you want verified NXP, Seritag 29 mm NTAG213 works too, because the daemon only reads the UID |
| Pololu D36V28F5 | Pololu $23.95, **out of stock**, backorder. RobotShop $21.95, restocking. Amazon (GetFPV) **$16.99 + $4.99** = $21.98, in stock. Mouser doesn't carry it; DigiKey blocked by CAPTCHA | Superseded 11/27: **Adafruit MPM3610** (#4739, $6.95) is enough for the capped LEDs |
| USB-C PD charger 45 W+, 15 V ⎓ 3 A | UGREEN Nexode 65W $22.49 (lists 15V/3A), Anker Nano 70W $32.99 (lists 15V⎓3A), Anker 65W 3-port $22.77 (15 V not stated in listing) | **UGREEN Nexode 65W** |
| SanDisk High Endurance 64 GB | Amazon $25.99, but **minimum order 2**; PiShop $30.95 | **PiShop** (rides along with Cart 1) |
| 19 mm latching switch | Adafruit: none rated for 12–15 V. Mouser: Bulgin only, $32–65. Amazon APIELE 10 A $13.49 | **Amazon APIELE** |

### Consolidation

- **Pi + Amp4 + SD card + heatsink at PiShop** (done): one shipment instead of three. Ordering the Amp4 from hifiberry.com
  would cost more after FedEx and wait on Swiss post and customs.
- **Pololu cart dropped**: the 5 V buck is now the Adafruit MPM3610 in the Adafruit cart. **DigiKey/Mouser shrank to one $2.34 encoder** costing $8.49 to ship;
  the 19 mm switch and the fuse holder went to Amazon. If DigiKey works for you after the CAPTCHA, check whether it
  ships the encoder cheaper; otherwise the Mouser cart is ready.
- **Wood moved from Rockler to Woodcraft.** Same items cost $13.50 more before shipping (Rockler had plywood on sale: $29.24 vs
  $38.99 for ½"), but Woodcraft ships free over $50 and has a Grand Rapids store for maple and pickup. Rockler would have
  been $108.44 with shipping vs $121.95 at Woodcraft. Rockler's cart was emptied so nothing is bought twice.
- **Buy the finish, maple and any bits at Woodcraft too**, online (free shipping) or at the Grand Rapids store.
- **Home Depot (Walker) has no true Baltic birch**, only birch-faced "PureBond", ProWood and Sande panels with softer cores.
  Fine for jigs and test cuts, not for the box. Lowe's wasn't checked.
- **Parts Express is $42 short of free shipping** ($99). Moving the 18 AWG speaker wire there (Consolidated 25 ft, $9.98) doesn't
  close the gap; paying the $9.95 is cheaper.
- **Adafruit is far from its $200 threshold**; moving the Pi there ($120) would cost more than the shipping it saves.
- **Adafruit + Mouser in one Mouser order (checked 11/27):** every Adafruit line is in stock at Mouser at the same price except
  the USB-C cable (+$2.49), and the combined order would ship free. But Adafruit's 15% code (−$10.23) cancels most of that,
  so the saving is only ~$0–5 depending on Adafruit's shipping. Kept as two orders.

### Still to buy (not in any cart)

| Item | Why not added | Suggested |
|---|---|---|
| Water-based toy-safe finish (EN 71-3 / ASTM F963) | Rockler and Woodcraft list no water-based finish with that label online. Rockler's only EN71 hit is Natura Onecoat Wood Oil 2K ($39.99), an oil | Your call. Ask at Woodcraft of Grand Rapids, or consider Osmo or a General Finishes water-based topcoat if you accept its toy-safe statement |
| Maple or cherry, ¾" and ½", 3–4 bd-ft | Sold by the board foot in store | Woodcraft of Grand Rapids or a local hardwood dealer, ~$30–50 |
| Perforated grille sheet, ~2 mm holes | Parts Express has none; McMaster's smallest is 24×24" ($54+) | Amazon 12×12" perforated stainless, ~$18 (3 mm holes on the listings that state size) |
| Router bits (⅜" and ¼" roundover, 45° chamfer), 1-⅜", 15/16" and ⅞" Forstners, 6 mm brad-point | Marked "if not owned". No hole saw needed now | ~$80–100 at Woodcraft |
| Polyester fiberfill, a handful | Removed from Parts Express (1 lb was ~30× too much) | Pillow or craft-stash polyester (not cotton or wool), or a small craft bag, ~$5 |
| Omron D2F-01L3 microswitch | Optional, only if the slot test fails | Mouser or DigiKey, ~$3 |

### Total versus the ≈ $820 estimate

| | Estimate | Real |
|---|---|---|
| Electronics (E1–E21, incl. charger and tags) | ≈ $460 | **≈ $431** (PN532 and charger already owned; 60 tags for two per cartridge; Pi +$40, Amp4 +$33, SD +$16, wiring small parts +$15, knob +$6; PN532 −$31, 5×8 LEDs −$7, 5 V buck −$10, one tag pack, pre-crimped JST, no speaker wire) |
| Enclosure and hardware in carts (printing supplies saved for later, $39) | | ≈ $121 (handle dowel, second ½" sheet and polyfill dropped) |
| Known shipping and tariff | | ≈ $19 (+ ≈ $25 still unpriced at PiShop, Adafruit, McMaster) |
| Not yet bought: finish, maple, grille sheet | | ≈ $90 |
| Tools, if not owned | | ≈ $90 |
| **Total** | **≈ $820** | **≈ $776 all-in** (≈ $686 if you already own the bits). The [cost-review.md](cost-review.md) savings were applied on 2026-11-27 (≈ $109); you already own a soldering kit |

## Final purchase checklist

Work through this before checking out. Add to it as questions come up.

- [ ] **Amp4 power jack (Adafruit #369, $2).** #369 is a 5.5 × 2.1 mm barrel plug with screw terminals. It carries
      the 15 V wires (HUSB238 → fuse → power switch) into the Amp4. Before buying:
  - Confirm the Amp4's input is a **5.5 × 2.1 mm** barrel jack. HiFiBerry's datasheet doesn't say; one retailer
    lists 5.5 × 2.1. Measure it or check HiFiBerry's docs. If the Amp4 uses screw terminals instead, remove #369.
  - Polarity: **centre pin positive**. The 15 V wire goes to the + terminal.
  - At assembly: tighten the screws firmly and cable-tie the wires to the sled so nothing tugs on the terminals.
