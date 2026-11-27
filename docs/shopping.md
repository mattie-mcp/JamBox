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

Carts built in Chrome on **2026-11-24** (add to cart only; nothing bought). Prices are what each cart showed that
day; several are Black Friday sale prices. Shipping marked "at checkout" needs an address, which was not entered.

| Cart | Store | Items in stock | Subtotal | Shipping | Free-ship threshold | Notes |
|---|---|---|---|---|---|---|
| 1 | [PiShop.us](https://www.pishop.us/cart.php) | 3/3 | $232.35 | At checkout (USPS / FedEx) | None listed | SD card moved here from Amazon |
| 2 | [Adafruit](https://www.adafruit.com/shopping_cart) | 7 lines; 74AHCT125 #1787 now out of stock (moved to Mouser); PN532 #364 and encoder #377 **out of stock** | $61.30 | At checkout | $200 (US) | No 19 mm latching switch rated for 12–15 V |
| 3 | [Parts Express](https://www.parts-express.com/cart) | 3/3 | $56.94 | $9.95 | $99 | Code EARLYBF15: 15% off $75+, ends 11/26 |
| 4 | Pololu | **0/1** (D36V28F5 out of stock, backorder only) | n/a | n/a | n/a | Bought on Amazon instead (Cart 6) |
| 5 | [Mouser](https://www.mouser.com/Cart/) (DigiKey showed a CAPTCHA) | 2/2 | $3.29 | $8.49 UPS Ground + $0.49 tariff | n/a | Switch and fuse moved to Amazon; level shifter added 11/27 |
| 6 | [Amazon](https://www.amazon.com/gp/cart/view.html) | 17/17 lines (18 units) | $214.37 | $4.99 (GetFPV regulator); rest free (Prime) | Prime | SanDisk card not added: 2-card minimum |
| 7 | [McMaster-Carr](https://www.mcmaster.com/order/) | 3/3 | $30.36 | At checkout | n/a | Perforated sheet not added (24×24" minimum, $54+) |
| 8 | [Woodcraft](https://www.woodcraft.com/cart) | 4/4 | $121.95 | Free (over $50, through Dec 1) | $50 | Switched from Rockler (cart emptied). Woodcraft of Grand Rapids is local for maple and pickup. Finish and tools not added (see below) |
| | **hifiberry.com** | comparison only | $64.90 | $38.00 FedEx | | Amp4 left in that cart for comparison; **remove it, don't buy both** |

**In carts: $720.56 of merchandise plus $23.92 of known shipping ≈ $745.** PiShop, Adafruit and McMaster shipping (≈ $25)
and sales tax come on top.

### Line items

| Cart | Item (exact title) | Part / SKU | Unit | Qty | Stock | Link |
|---|---|---|---|---|---|---|
| 1 | Raspberry Pi 4 Model B/4GB | PiShop 4GB-9004 (SC0194) | $100.00 | 1 | In stock | [pishop](https://www.pishop.us/product/raspberry-pi-4-model-b-4gb/) |
| 1 | ↳ add-on: Aluminum Heatsink for Raspberry Pi 4B (3-Pack) | PiShop 1723 | $2.95 | 1 | In stock | same page |
| 1 | HiFiBerry AMP4 | PiShop 23-1 | $98.45 | 1 | In stock | [pishop](https://www.pishop.us/product/hifiberry-amp4/) |
| 1 | SanDisk High Endurance MicroSDXC Card - 64GB - Class10 - BLANK | SanDisk High Endurance 64GB | $30.95 | 1 | In stock | [pishop search](https://www.pishop.us/search.php?search_query=sandisk+high+endurance+64gb) |
| 2 | Adafruit USB Type C Power Delivery Dummy Breakout - I2C or Fixed - HUSB238 | #5807 | $5.95 | 1 | In stock | [adafruit](https://www.adafruit.com/product/5807) |
| 2 | Adafruit NeoPixel NeoMatrix 8x8 - 64 RGB LED Pixel Matrix | #1487 | $34.95 | 1 | In stock | [adafruit](https://www.adafruit.com/product/1487) |
| 5 | Texas Instruments SN74AHCT125N quad buffer, DIP-14 (same chip as Adafruit #1787, which went out of stock 11/27) | Mouser 595-SN74AHCT125N | $0.95 | 1 | 1,002 in stock | [mouser](https://www.mouser.com/c/?q=SN74AHCT125N) |
| 2 | Stacking Header - 2x20 Extra Tall Header | #1979 | $2.95 | 1 | In stock | [adafruit](https://www.adafruit.com/product/1979) |
| 2 | Arcade Button with LED - 30mm Translucent Blue / Green / Yellow | #3490 / #3487 / #3488 | $2.50 | 1 each | In stock | [adafruit](https://www.adafruit.com/product/3490) |
| 2 | USB C Round Panel Mount Extension Cable | #4218 | $9.95 | 1 | In stock | [adafruit](https://www.adafruit.com/product/4218) |
| 3 | Dayton Audio PC83-4 3" Full-Range Poly Cone Driver | 295-154 | $15.49 | 2 | 1,074 in stock | [parts-express](https://www.parts-express.com/Dayton-Audio-PC83-4-3-Full-Range-Poly-Cone-Driver-295-154) |
| 3 | Parts Express Speaker Grille Cloth Black Yard 70" Wide | 260-335 | $9.98 | 1 | In stock | [search](https://www.parts-express.com/search?keywords=260-335) |
| 3 | Acousta-Fill Nylon Polyfill 1 lb. Bag | 260-319 | $15.98 | 1 | In stock | [search](https://www.parts-express.com/search?keywords=260-319) |
| 5 | Bourns PEC11R-4220F-S0024 Encoders 20mm SHAFT w/SWITCH | Mouser 652-PEC11R-4220F-S24 | $2.34 | 1 | 8,085 in stock | [mouser](https://www.mouser.com/ProductDetail/Bourns/PEC11R-4220F-S0024) |
| 6 | 5V, 3.2A Step-Down Voltage Regulator D36V28F5 (sold by GetFPV) | B0BJKVWR2D | $16.99 | 1 | In stock | [amazon](https://www.amazon.com/dp/B0BJKVWR2D) |
| 6 | HiLetgo PN532 NFC NXP RFID Module V3 Kit | B01I1J17LC | $8.99 | 1 | In stock | [amazon](https://www.amazon.com/dp/B01I1J17LC) |
| 6 | 30pcs NFC Tags NTAG215 NFC Coins Rewritable White NFC Tag Round 30mm | B07PFC2FH5 | $9.50 | 2 | In stock | [amazon](https://www.amazon.com/dp/B07PFC2FH5) |
| 6 | UGREEN Nexode 65W USB C Charger Block, 3-Port (lists 15V/3A) | B091BGMKYS | $22.49 | 1 | In stock | [amazon](https://www.amazon.com/dp/B091BGMKYS) |
| 6 | APIELE 10 Amp 19mm Latching Push Button Switch 12V SPST LED (stainless, blue ring) | B07V96FYHP | $13.49 | 1 | In stock | [amazon](https://www.amazon.com/dp/B07V96FYHP) |
| 6 | 2pcs 18AWG Inline Fuse Holder with 3A Mini Fuse | B0DC3LVV75 | $5.59 | 1 | In stock | [amazon](https://www.amazon.com/dp/B0DC3LVV75) |
| 6 | 2020-Piece JST XH 2.54mm Connector Kit with Ratcheting Crimping Tool | B0G2L3LGWD | $23.74 | 1 | In stock | [amazon](https://www.amazon.com/dp/B0G2L3LGWD) |
| 6 | TUOFENG 22 AWG Silicone Wire Kit, 6 Colors, 26.3 ft Each | B07G2JWYDW | $15.99 | 1 | In stock | [amazon](https://www.amazon.com/dp/B07G2JWYDW) |
| 6 | RCA AH1850N 50 feet 18-Gauge Speaker Wire | B00005T3G2 | $7.99 | 1 | Only 9 left | [amazon](https://www.amazon.com/dp/B00005T3G2) |
| 6 | 365 Pcs M2.5 Black Nylon Hex Standoff Screw Nut Kit | B0FPMC9917 | $9.99 | 1 | In stock | [amazon](https://www.amazon.com/dp/B0FPMC9917) |
| 6 | HANGLIFE Heat-Set Threaded Inserts, M3 x D5 x L4 (100 pcs) | B0CS6VZYL8 | $8.99 | 1 | In stock | [amazon](https://www.amazon.com/dp/B0CS6VZYL8) |
| 6 | smseace 100PCS (5 Sizes) Rubber Feet with Washer and Screws | B08PBH875X | $9.99 | 1 | In stock | [amazon](https://www.amazon.com/dp/B08PBH875X) |
| 6 | PEI Flexi Steel Magnetic Build Plate 235×235 (Ender 3 Pro; includes magnetic base) | B09WZSGXFL | $15.99 | 1 | In stock | [amazon](https://www.amazon.com/dp/B09WZSGXFL) |
| 6 | SUNLU PETG Filament 1.75mm, 1kg, Black | B0DJS3PJVX | $11.96 | 1 | In stock | [amazon](https://www.amazon.com/dp/B0DJS3PJVX) |
| 6 | SUNLU PLA 3D Printer Filament, Black, 1KG | B07XG3RM58 | $11.19 | 1 | In stock | [amazon](https://www.amazon.com/dp/B07XG3RM58) |
| 6 | Szliyands 44 x 25mm Aluminum Knob for 6 mm Shaft (set screw + wrench); backup if you don't print or turn one | B099DHHGGQ | $11.99 | 1 | In stock | [amazon](https://www.amazon.com/dp/B099DHHGGQ) |
| 7 | Tamper-Resistant Torx 18-8 SS Button Head Screws, M3 x 0.5 x 10 mm (pack of 50) | 91900A848 | $12.54 | 1 | Delivers tomorrow | [mcmaster](https://www.mcmaster.com/91900A848/) |
| 7 | Tamper-Resistant Torx Bit, 1/4" Hex Shank, T8 | 7233A61 | $7.84 | 1 | Delivers tomorrow | [mcmaster](https://www.mcmaster.com/7233A61/) |
| 7 | Moisture-Resistant HDPE Sheet 12" x 12" x 1/4" (FDA) | 8619K461 | $9.98 | 1 | Delivers tomorrow | [mcmaster](https://www.mcmaster.com/8619K461/) |
| 8 | Woodcraft Woodshop Baltic Birch Plywood, 1/2" x 30" x 30" | Woodcraft #191388 | $38.99 | 2 | In stock online | [woodcraft](https://www.woodcraft.com/products/woodcraft-woodshop-baltic-birch-plywood) |
| 8 | Woodcraft Woodshop Baltic Birch Plywood, 1/4" x 30" x 30" | Woodcraft #191387 | $21.99 | 1 | In stock online | same page |
| 8 | Titebond III Ultimate Wood Glue - Waterproof, 16-oz | Woodcraft #145562 | $9.99 | 1 | In stock online | [woodcraft](https://www.woodcraft.com/products/titebond-iii-ultimate-wood-glue-waterproof) |
| 8 | Cindoco 36" Round Wood Dowel, Maple, 1" | Woodcraft #158597 | $11.99 | 1 | In stock online | [woodcraft](https://www.woodcraft.com/products/cindoco-36-round-wood-dowel) |

### Comparisons

| Item | Options (Nov 24, 2026) | Recommended |
|---|---|---|
| Pi 4 4 GB | PiShop **$100**, CanaKit $100, Micro Center $99.99 (in-store pickup only), Adafruit $120 | **PiShop**: same price as CanaKit, ships with the Amp4 and SD card |
| HiFiBerry Amp4 | PiShop **$98.45**, in stock, ships with the Pi. hifiberry.com $64.90 + $38.00 FedEx Intl Economy = **$102.90**, plus possible US duties, 1–6 weeks | **PiShop** |
| PN532 | Adafruit #364 $39.95, **out of stock**. Amazon V3 clones: HiLetgo $8.99 (220 reviews), AITRIP $7.99. No Elechouse-branded listing on Amazon | **HiLetgo V3** (in cart). Same PN532 chip and I2C, so the code works unchanged |
| NTAG215, 30–35 mm | **ShopNFC: no NTAG215** (stocks 210/213/216/DNA; e.g. NTAG213 Bullseye 38 mm €0.69). **Seritag: no NTAG215**; genuine-NXP NTAG213 29 mm **$0.37** (10–99). Amazon: 30 mm NTAG215 coins, 30-pack $9.50 = **$0.32/tag** (genuine NXP not stated); most Amazon 50-packs are 25 mm | **Amazon 30 mm coins** (2 packs = 60 tags, in cart). If you want verified NXP, Seritag 29 mm NTAG213 works too, because the daemon only reads the UID |
| Pololu D36V28F5 | Pololu $23.95, **out of stock**, backorder. RobotShop $21.95, restocking. Amazon (GetFPV) **$16.99 + $4.99** = $21.98, in stock. Mouser doesn't carry it; DigiKey blocked by CAPTCHA | **Amazon / GetFPV** |
| USB-C PD charger 45 W+, 15 V ⎓ 3 A | UGREEN Nexode 65W $22.49 (lists 15V/3A), Anker Nano 70W $32.99 (lists 15V⎓3A), Anker 65W 3-port $22.77 (15 V not stated in listing) | **UGREEN Nexode 65W** |
| SanDisk High Endurance 64 GB | Amazon $25.99, but **minimum order 2**; PiShop $30.95 | **PiShop** (rides along with Cart 1) |
| 19 mm latching switch | Adafruit: none rated for 12–15 V. Mouser: Bulgin only, $32–65. Amazon APIELE 10 A $13.49 | **Amazon APIELE** |

### Consolidation

- **Pi + Amp4 + SD card + heatsink at PiShop** (done): one shipment instead of three. Ordering the Amp4 from hifiberry.com
  would cost more after FedEx and wait on Swiss post and customs.
- **Pololu cart dropped**: the regulator ships from Amazon. **DigiKey/Mouser shrank to one $2.34 encoder** costing $8.49 to ship;
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

### Still to buy (not in any cart)

| Item | Why not added | Suggested |
|---|---|---|
| Water-based toy-safe finish (EN 71-3 / ASTM F963) | Rockler and Woodcraft list no water-based finish with that label online. Rockler's only EN71 hit is Natura Onecoat Wood Oil 2K ($39.99), an oil | Your call. Ask at Woodcraft of Grand Rapids, or consider Osmo or a General Finishes water-based topcoat if you accept its toy-safe statement |
| Maple or cherry, ¾" and ½", 3–4 bd-ft | Sold by the board foot in store | Woodcraft of Grand Rapids or a local hardwood dealer, ~$30–50 |
| Perforated grille sheet, ~2 mm holes | Parts Express has none; McMaster's smallest is 24×24" ($54+) | Amazon 12×12" perforated stainless, ~$18 (3 mm holes on the listings that state size) |
| Router bits, 3" hole saw, 1-⅜" Forstner, 6 mm brad-point | Marked "if not owned" | ~$80–100 at Woodcraft |
| Omron D2F-01L3 microswitch | Optional, only if the slot test fails | Mouser or DigiKey, ~$3 |

### Total versus the ≈ $820 estimate

| | Estimate | Real |
|---|---|---|
| Electronics (E1–E21, incl. charger and tags) | ≈ $460 | **≈ $494** (Pi +$40, Amp4 +$33, SD +$16, knob +$12; PN532 −$31) |
| Enclosure, printing supplies, hardware in carts | | ≈ $227 |
| Known shipping and tariff | | ≈ $24 (+ ≈ $25 still unpriced at PiShop, Adafruit, McMaster) |
| Not yet bought: finish, maple, grille sheet | | ≈ $90 |
| Tools, if not owned | | ≈ $90 |
| **Total** | **≈ $820** | **≈ $950 all-in** (≈ $860 if you already own the bits and hole saw); still under the $1000 budget |
