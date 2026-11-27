# JamBox v2 cost review

> **Applied 2026-11-27.** Rows 1–5 and 7–8 are in the carts (≈ $109 saved): one ½" sheet, the Adafruit MPM3610 buck,
> no polyfill bag, one tag pack (later back to two for the two-tag cartridges), a pre-crimped JST kit, no speaker wire, the Woodcraft maple knob. Row 6 was checked and
> skipped (Adafruit's 15% code makes one Mouser order save only ~$0–5). Row 9: kept the Amazon feet kit, which is already
> screw-on. The missing small parts (proto HAT, 1000 µF, 330/470 Ω, 0.1 µF, DC plug, heat-shrink) are in the Mouser
> and Adafruit carts. The owner already has a soldering kit. See [shopping.md](shopping.md) for the current carts.

Research only, 2026-11-27. Nothing was added to, removed from or bought in any cart. Prices come from the carts
in [shopping.md](shopping.md) (Results, 2026-11-24/27) unless a row gives a new source. A price marked
**unverified** could not be confirmed on the store's own page today (Amazon, Mouser and Newegg blocked automated
reads; Woodcraft rate-limited).

## Summary

About **$113 of realistic savings (≈ 12% of the ≈ $945 all-in)** without touching the look or toddler safety.
Most of it comes from five places: one ½" Baltic birch sheet instead of two ($39), a smaller 5 V regulator that
rides in the Adafruit order ($15), polyfill bought by the handful instead of the pound (~$11), 30 NFC tags instead
of 60 ($9.50), and dropping the 18 AWG speaker wire, the JST crimper kit and a shipping charge by consolidating
(~$27). A second ~$77 is available only if you already own the item: wire, standoffs, heat-set inserts, glue, a
spare cutting board, a spare 45 W+ PD charger. That would take the saving to ~$190 (≈ 20%). The 3D-printing
supplies (PEI sheet, PETG, PLA: $39.14) are being pulled from the Amazon cart and are left out of all these
totals. On the other side, the carts are **missing about $10–15 of small parts** the wiring needs (proto board for
the JST headers, the 1000 µF cap and 330 Ω resistor, a 5.5 × 2.1 mm DC plug for the Amp4, heat-shrink). Budget for
those out of the savings. The knobs and switches are already near the floor: the one design-led win is a maple knob.

## Ranked opportunities

Ranked by realistic saving, weighted by confidence. Only rows 1–9 count toward the $113.

| # | Item(s) | Now: store, price | Proposed change (part, store, price, URL) | Saving | Design impact | Safety impact | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | ½" Baltic birch, 30 × 30" | Woodcraft #191388, 2 × $38.99 | **Buy one sheet.** All the 12 mm Radio parts fit on one 30 × 30" panel (≈ 760 × 760 mm) with ~200 mm to spare: a 200 mm strip for the front and back (360 + 360), a 200 mm strip for both sides (146 + 146) and the top (336 × 146), a 146 mm strip for the bottom (336). That's ≈ 0.30 m² of 0.58 m². Woodcraft stays over $50 free shipping ($82.96). Woodcraft Grand Rapids is local if a part needs recutting. [woodcraft](https://www.woodcraft.com/products/woodcraft-woodshop-baltic-birch-plywood) | **$38.99** | None, if the face grain is planned on the layout. The cartridge garage may need offcuts or a second sheet later | None | High |
| 2 | 5 V regulator for the LEDs | Amazon (GetFPV) Pololu D36V28F5, $16.99 + $4.99 ship | **Adafruit MPM3610 5 V buck, 6–21 V in, 1.2 A out (#4739), $6.95**, in stock, in the Adafruit order. The LEDs are capped at ~20% (≈ 0.48 A worst case) plus the level shifter, so 1.2 A leaves 2.5× headroom. Removes the GetFPV shipping. [adafruit 4739](https://www.adafruit.com/product/4739) | **$15.03** | None (hidden on the sled) | Neutral to positive: a software bug at 100% brightness (2.4 A) gets current-limited instead of supplied. The MPS module datasheet lists current-limit and thermal shutdown. That's not stated on Adafruit's page, so check it. 15 V in is inside its 21 V limit | High (price), medium (it changes a decided part) |
| 3 | Polyfill | Parts Express Acousta-Fill 1 lb (260-319), $15.98 | The two ~1 L chambers need roughly half an ounce loosely stuffed. A 1 lb bag is ~30× that. **Use polyester fill you already have** (pillow, craft stash), or a small craft bag of polyester fiberfill (~$5, **unverified**) | **~$11** ($15.98 if owned) | None (inside sealed chambers) | None. Keep it polyester (not cotton or wool) | Medium |
| 4 | NFC tags | Amazon 30 mm NTAG215 coins B07PFC2FH5, 2 × $9.50 | **One 30-pack.** The garage holds 10 cartridges; 30 tags covers 10 cartridges, a top-end second tag on each (optional) and 10 spares. Buy more later at $0.32 each | **$9.50** | None | None | High |
| 5 | JST-XH kit with crimper | Amazon 2020-piece kit with ratcheting crimper B0G2L3LGWD, $23.74 | The box needs **7–8 housings and ~28 crimps** (see the wiring BOM). Swap for a **JST-XH kit with pre-crimped single-ended leads** (2–7 pin housings and headers, ~90–100 × 22 AWG leads crimped one end and tinned the other; no crimper). Examples: [Newegg 2–7 pin, 90 pre-crimped](https://www.newegg.com/p/0SV-00U8-000F4), [Newegg 2–10 pin, 100 × 22 AWG](https://www.newegg.com/p/0SV-00U8-000F3); same style on Amazon. ~$12–14, **unverified**. Check the lead length is ≥ 30 cm for the encoder run, or splice. **If you own an SN-28B/Dupont crimper, skip the kit** and buy only XH housings and pins (~$8, unverified) | **~$10** ($23.74 if you own a crimper and housings) | None | None: still keyed XH connectors everywhere | Medium-low (price unverified) |
| 6 | Adafruit + Mouser shipping | Mouser $3.29 + $8.49 UPS + $0.49 tariff; Adafruit $54.30 + shipping at checkout (unpriced) | **One Mouser order** for the encoder and SN74AHCT125N you're keeping at Mouser, plus the Adafruit lines. Mouser resells Adafruit (HUSB238 is Mouser 485-5807 at $5.95; #1430, #1979, #3490/3487/3488, #4218, #4739 need checking). At ≈ $64 the order clears Mouser's US free-shipping threshold (**$50, unverified for 2026**). Add the 1000 µF cap, 330 Ω resistor and a proto board to the same order. If any Adafruit part is missing or dearer at Mouser, keep the two orders | **$8.98** (+ ~$6–10 Adafruit shipping, unverified) | None | None | Medium-low |
| 7 | 18 AWG speaker wire | Amazon RCA AH1850N 50 ft, $7.99 | **Drop it.** Each speaker run is ~30 cm. 22 AWG twisted pair from the hookup-wire kit (or the pre-crimped leads) adds ≈ 0.03 Ω against a 4 Ω driver (< 0.1 dB) at toddler volume. The other 49 ft would go unused | **$7.99** | None | None (a few watts at most) | High |
| 8 | Volume knob | Amazon Szliyands 44 × 25 mm aluminium knob B099DHHGGQ, $11.99 | **Cindoco maple Shaker knob, 2" (51 mm) dia, ¾" tenon, 2-pack, Woodcraft, $5.99** (search snapshot, **unverified** live). It rides in the free-shipping Woodcraft cart. Cut the tenon short, drill 6 mm axially, epoxy onto the PEC11R D-shaft, and finish with the toy-safe finish. The second knob is a spare. Or make one free from a cartridge offcut: a ≥ 40 mm disc of ¾" maple. [woodcraft](https://www.woodcraft.com/products/cindoco-shaker-knob-maple-2-diameter-3-4-tenon-2-piece) | **$6.00** ($11.99 if made from offcut) | **Better**: maple matches the cartridges, and a mushroom radio-knob shape suits the Jam Radio | Same or better: 51 mm can't fit the 31.7 mm small-parts cylinder. It's lighter and has no set screw to work loose. Glue it and pull-test it | Medium |
| 9 | Rubber feet | Amazon smseace 100-pc, 5-size kit with screws, $9.99 | **Four screw-on rubber bumpers, ~10 mm tall**, from a hardware store (~$4, **unverified**), or add them to the McMaster order. Keep them **screwed**, not adhesive | **~$6** | None | Same, if screwed (see "don't cut") | Medium |
| 10 | McMaster order | Torx screws 91900A848 $12.54, T8 bit 7233A61 $7.84, HDPE 8619K461 $9.98, + shipping at checkout | Option: HDPE from a spare or $5–8 plain **HDPE cutting board** (shopping.md already allows this), and M3 pin-in Torx button heads with a matching bit from Amazon (~$8–10, **unverified**) to drop the McMaster shipment | ~$5–15 (not counted) | None | Watch quality: McMaster's 18-8 parts are a known quantity; Amazon kits vary. Must be pin-in (tamper-resistant), not plain Torx | Low |
| 11 | 19 mm latching power switch | Amazon APIELE 10 A, B07V96FYHP, $13.49 | **Keep.** Comparable 19 mm stainless latching ring-LED switches rated 5–10 A run $13–15 (e.g. a Keegwa 2-pack at Walmart, $13.95, out of stock; NOFUEL on eBay $13.99). Mouser only has Bulgin at $32–65. A 16 mm switch is cheaper but looks undersized | $0 | — | Check the ring LED: a "12 V" ring on 15 V draws ~1.5× its rated current. Add a ~330–470 Ω series resistor, or buy the 12–24 V ring variant | Medium |
| 12 | Arcade buttons, encoder, USB-C panel mount | Adafruit #3490/3487/3488 3 × $2.50; Mouser PEC11R $2.34; Adafruit #4218 $9.95 | **Keep.** Non-LED 30 mm buttons save ~$0.50 each and lose the glow. #4218 is the right part (21.5–27 mm hole, ≤ 16 mm panel, 30 cm). Its listing gives no current/PD rating, so bench-test 15 V/3 A through it first | $0 | — | — | High |

Not counted in the $113 (conditional "if you have it, skip it"; a 3D-printer and woodworking hobbyist often does):

| Item | Cart price | Notes |
|---|---|---|
| 22 AWG silicone wire kit (TUOFENG 6 × 26 ft) | $15.99 | The box needs ~6 m (≈ 20 ft) in total. Any stranded 20–24 AWG works, and a spare **Ethernet patch cable** gives colour-coded 24 AWG twisted pairs for the buttons, encoder and PN532. Keep ≥ 22 AWG (or doubled pairs) for the 15 V path. If you don't own wire, this kit is good value per foot; smaller kits cost about the same |
| M2.5 nylon standoff kit | $9.99 | Needed: 4 × ~10 mm for Pi-to-sled. The Amp4 ships with its own mounting parts, but the **extra-tall stacking header raises it, so its spacers may be too short**. An assorted kit you already own covers both |
| M3 heat-set inserts (100) | $8.99 | Needed: ~6–8 for the service cover plus any printed brackets. Heat-set inserts are for plastic; in plywood, **epoxy them in** or use M3 wood (knife) inserts |
| Heat-shrink | not in any cart | Needed at every solder joint |
| Titebond III | $9.99 | |
| HDPE sheet | $9.98 | A spare plain HDPE cutting board |
| USB-C PD charger | $22.49 | Only if a spare 45 W+ charger **listing 15 V ⎓ 3 A** can stay with the box |
| Router bits, hole saw, Forstners (~$90 "if not owned") | — | A 3D-printed router circle-cutting jig can replace the 3" hole saw for the two driver holes |
| **Total if all owned** | **≈ $77** (excluding the charger: ≈ $55) | |

Already decided or noted: the maintenance kit is skipped; 3D-printing supplies (PEI sheet $15.99, PETG $11.96,
PLA $11.19 = $39.14) are being pulled from the Amazon cart and are not in these totals. Parts Express code EARLYBF15
expired 11/26, and Parts Express can't reasonably reach $99 free shipping, so pay the $9.95. The hifiberry.com
comparison cart should be emptied. The SanDisk High Endurance card ($30.95) looked like a saving at first, but
high-endurance card prices are all over the place this year (Walmart/Newegg $25.98 for 32 GB, Samsung PRO
Endurance 64 GB $14.99 on an undated Samsung page). Compare the day you buy; no saving is counted.

## Don't cut

- **Loose Dupont jumpers instead of keyed JST-XH.** They shake loose in the drop test, and an unkeyed plug can put
  15 V or 5 V on a 3.3 V pin. Keyed connectors are what let the sled slide out safely.
- **Adhesive rubber feet.** A toddler can peel them off, and a 10–20 mm foot fits the small-parts cylinder. Use screwed
  feet. Don't drop the feet either: their 10 mm gap is the bottom vent inlet.
- **A 1" dowel offcut as the knob.** At 25 mm it **fits the 31.7 mm small-parts cylinder**, a choking hazard if it ever
  comes off. The knob must stay ≥ 40 mm across (the 2" Shaker knob is 51 mm).
- **Wooden caps glued onto the arcade buttons.** They'd look nice, but they turn a one-piece plunger into a pryable
  cap under 31.7 mm. Keep the stock translucent caps; their glow is part of the design anyway.
- **A plastic rocker, toggle or momentary switch for power.** Rockers and toggles can be snapped or pried. A
  momentary switch can't hold power without a latch circuit. The stainless anti-vandal latching switch is the toddler-proof
  part, and its ring is the "on" light.
- **The inline fuse.** It's $5.59. Keep it (a 2 A fuse would be a closer fit than 3 A for a ~1.3 A worst-case load).
- **No-name LM2596/MP1584 buck modules or generic PD-trigger boards.** Counterfeit regulators and missing protection.
  If the regulator changes, go to a known part (Adafruit/MPS) as in row 2.
- **The steel mesh behind the grilles.** It's what keeps small fingers and pencils out of the driver cones (6 mm holes
  alone aren't enough). The ~$18 perforated sheet still to buy stays in the budget.
- **Non-Baltic "birch" ply (Home Depot) or thinner stock to save on the second sheet.** Cutting to one sheet is fine;
  downgrading the sheet is not.
- **Smaller or cheaper tags** (25 mm, or the cheapest on-metal/odd chips). Range drops through the 18–20 mm gap.
- **The toy-safe finish, and a certified charger that lists 15 V ⎓ 3 A.** An uncertified or 5 V-only brick either
  leaves the box dead or is a fire risk on a nursery floor.
- **Non-LED arcade buttons.** Saves ~$1.50 total, loses the lit buttons.

## Wiring bill of materials

Geometry from [enclosure.md](enclosure.md): 360 × 170 × 200 mm box, 144 mm centre bay (layout revised 2026-11-27), sled on rails sliding
out the back, drivers at the far ends, LED window front-upper, buttons front-lower, encoder top back-right, PN532 on the
slot sleeve, USB-C and power button in the 12 mm back panel above the service opening. Every run gets a **JST-XH plug at the sled end** so the
sled unplugs without tools. The far end is soldered and heat-shrunk.

| Run | From → to | Conductors | Length (each) | Sled connector | Far end | Notes |
|---|---|---|---|---|---|---|
| Speaker L | Amp4 speaker terminal → left driver | 2 (twisted) | ~30 cm | XH 2-pin | Solder to driver tabs | Pass through the sealed chamber wall, caulked |
| Speaker R | Amp4 → right driver | 2 (twisted) | ~30 cm | XH 2-pin | Solder | |
| 15 V in | Back panel → sled | 2 (or 4: V, V, G, G) | ~20 cm | XH 2- or 4-pin | Cover sub-assembly | Mount the HUSB238, fuse and switch **on the back panel**, above the service opening. USB-C #4218 → HUSB238 is the extension cable itself (no wire). Switch ring LED wired at the cover (LED+ to the switched side, LED− to GND, plus a series resistor). ≥ 22 AWG or doubled pairs; XH is rated 3 A |
| 15 V split | On sled → Amp4 and the 5 V buck | 2 + 2 | ~10 cm | — | **5.5 × 2.1 mm DC plug** into the Amp4 jack (per [Audiophonics](https://www.audiophonics.fr/en/amplifier-and-headphone-amplifier-modules/hifiberry-amp4-p-19117.html); HiFiBerry's datasheet doesn't name the connector, so confirm) | DC plug not in any cart (~$1–2, or a pigtail) |
| LED matrix | Buck 5 V + level shifter → shield pads | 3 (5 V, GND, DIN) | ~20 cm | XH 3-pin | Solder to the shield's DIN/5 V/GND pads | 1000 µF across 5 V at the shield; 330 Ω in DIN. **Neither is in any cart** |
| PN532 | Pi I2C → sleeve back wall | 4 (3V3, GND, SDA, SCL) | ~20 cm | XH 4-pin | Solder to the V3 header pads | Keep the far end clear of metal |
| Buttons | Pi GPIO 23/24/25 → 3 arcade buttons | 5 (3 switch, common GND, LED+) | ~15 cm | XH 5-pin | Solder to the 24 mm buttons' switch and LED tabs (originally: 0.110" tabs or [Adafruit #1152](https://www.adafruit.com/product/1152) quick-connect pairs, $4.95, out of stock; [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/1152/7241453) lists 51) | LED+ to 5 V lights all three when on. Yellow needs 5 V (series LEDs). The GND jumpers daisy-chain between buttons |
| Encoder | Pi GPIO 17/27/22 → top-right | 4 (A, B, SW, GND) | ~30 cm | XH 4-pin | Solder to the PEC11R pins | The longest signal run |
| Slot switch (optional) | GPIO 5 → under the sleeve | 2 | ~15 cm | XH 2-pin | Solder | Only if the slot test fails |
| GPIO breakout | Stacking header → XH headers + 74AHCT125 | — | — | — | — | Needs a small proto board/Perma-Proto on the stacking header ("+ HAT" in E15). **Not in any cart** (~$5–8) |

**Totals:** 7 XH housings (8 with the slot switch): 2 × 2-pin, 1 × 2/4-pin, 1 × 3-pin, 2 × 4-pin, 1 × 5-pin, and the
matching board headers. That's **~24–28 crimped contacts**. Wire is **~6 m (≈ 20 ft)** across at least five
colours, all 22 AWG or 24 AWG except the 15 V path (≥ 22 AWG or doubled). There's no wire-to-wire XH joint, so
single-ended pre-crimped leads (crimp at the sled, solder at the device) cover every run.

## Decisions for the owner

1. **One ½" Baltic birch sheet or two?** One covers the Radio with ~200 mm spare. Keep two only if you want the
   cartridge garage and recut margin in the same order.
2. **Swap the 5 V regulator to the Adafruit MPM3610** (1.2 A, $6.95), or keep the Pololu 3.2 A for headroom (e.g.
   if the LED brightness cap may rise or the button LEDs grow)?
3. **Crimp or pre-crimped?** Keep the $23.74 kit with crimper (reusable tool), buy a pre-crimped XH lead kit (~$12–14),
   or use a crimper you already own.
4. **Knob:** Woodcraft 2" maple Shaker knob, a disc turned from cartridge maple, or the aluminium backup?
5. **Consolidate Adafruit into the Mouser order** (if Mouser has every part at Adafruit's price and the $50
   free-shipping threshold holds at checkout)?
6. **How many tags:** 30 now, more later?
7. **What you already own:** wire, heat-shrink, standoffs, heat-set inserts, Titebond III, a spare HDPE board, a
   spare 45 W+ PD charger, router bits and hole saw. Each one owned is a line deleted.
8. **Add the missing small parts** (1000 µF cap, 330 Ω, proto board, DC plug, heat-shrink, button connectors or
   solder) to whichever order survives, likely Mouser.
9. **McMaster vs Amazon** for the tamper-resistant screws and HDPE (small saving, some quality risk).
