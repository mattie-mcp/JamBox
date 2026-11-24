# Exploration: 3D-printed cartridges

**Status:** exploratory (stretch goal), on branch `claude/3d-printed-cartridges`.
**Printer on hand:** Creality Ender 3 Pro, plus other printers you can borrow.
**Models:** [`hardware/3d/`](../../hardware/3d/): parametric OpenSCAD sources plus ready-to-slice STLs.

The baseline cartridge in [enclosure.md](../enclosure.md) is a laminated hardwood block. This doc
works out whether a printed cartridge can match it for durability, and how to make it.

---

## 1. Hide the tag so it can't be peeled

Jamie already peels stickers off cartridges, so **no tag, label or sticker may sit on an outside
surface.** That applies to every cartridge type.

| Method | How | Notes |
|---|---|---|
| **Embed mid-print** (recommended for printed) | The model has a tag-shaped pocket at the centre of the thickness. Pause the print when the pocket is finished, drop in the tag, resume | The tag is fully enclosed in plastic. The pocket is exactly tag-deep, so the next layer prints onto the tag with no bridging |
| **Two halves glued** | Print `half a` (with pocket) and `half b`, glue them with the tag between, aligned by two printed pins | For when pausing is unreliable. The glue line runs around the edge; sand flush |
| **Hardwood glue-up** (wood baseline) | Tag in a 1 mm Forstner pocket at the glue line between two boards | Already in the main design; nothing visible |
| Pocket + plug | A blind hole from the back, tag in, then an epoxied printed or wood plug | Fallback for existing blocks. A determined toddler may find the plug edge |

**Artwork must also not be stickers.** Use a raised printed icon in a second colour (filament change),
paint sealed under finish, or engraving.

**Heat:** the nozzle lays hot plastic directly onto the tag. Embedding NTAG chips this way is a common
maker technique. Still, **prove it with one test print, then check that the tag reads afterwards** before
batching. PVC coin tags soften at low temperatures; PET or paper stickers and "wet inlay" tags are the safest to print over.

## 2. The models

All are in `hardware/3d/`. Open the `.scad` files in OpenSCAD to change parameters, or slice the `stl/` files directly.

| File | What | Print notes |
|---|---|---|
| `cartridge.scad` → `stl/cartridge_single_star.stl` | 80 × 100 × 30 mm block, 6 mm roundover, 1.2 mm raised star on the front, Ø35.6 × 1.0 mm tag pocket centred at mid-thickness, 33 mm up from the bottom | Lies on its flat back. **Pause at the first layer above z = 15.5 mm**, insert the tag, resume. Optional filament change at z = 30.0 for a 2-colour star |
| `stl/cartridge_half_a.stl`, `half_b.stl`, `pins.stl` | The same cartridge split in two (`mode="half"`) | Both halves print glue-face down. Icons on both faces |
| `nfc_gap_steps.scad` → `stl/nfc_gap_steps.stl` | Stepped spacer: 5, 10, 15, 20, 25, 30 mm pads with a tag outline, 120 × 120 mm | Set it on the PN532 and find the largest gap that reads reliably |
| `slot_mockup.scad` → `stl/slot_mockup.stl` | The slot sleeve: 34 × 84 mm opening, 60 mm deep, **6 mm walls** like the plywood, 45° lead-in, crumb hole, zip-tie slots to strap a PN532 to the wall | Tests fit, pull-out feel and NFC-only removal before building the box |

**Key parameters in `cartridge.scad`:**
- `tag_d`, `tag_t`: **measure your tags with calipers** and set these first.
- `tag_y`: tag height.
- `icon`: star / heart / circle / note / none.
- `icon_y`, `relief`.
- `both_faces`: half mode only.

The model echoes the exact pause height when rendered.

## 3. Will the Ender 3 Pro do it?

**Yes, with a few checks.** Every model fits its 220 × 220 × 250 mm bed. The biggest is the slot mock-up flange at 126 × 76 mm.

| Need | Ender 3 Pro reality | What to do |
|---|---|---|
| Durable material | PLA prints easily. **PETG** is tougher and less brittle for a toddler toy, but wants 230–245 °C | The stock PTFE-lined hotend is OK up to ~240 °C. Print PETG at the low end, or upgrade to an all-metal hotend or a Capricorn PTFE tube. "Tough PLA" or "PLA+" is a good middle ground |
| Bed release | PETG welds itself to bare glass | Use a **textured PEI spring-steel sheet**. It also gives the cartridge back a nice matte texture |
| Pause to insert the tag | Depends on firmware. Older stock Creality firmware may not support `M600` | Use Cura's **"Pause at height"** script (or PrusaSlicer's pause). **Do a 10-minute test print first** to confirm it pauses, parks and resumes cleanly. If not, use the two-halves mode |
| Two-colour icon | Single extruder | A colour change at one layer height gives a 2-colour icon on the front face. True multicolour characters need a multi-material printer |
| Levelling | Manual knobs | Re-level before a long print. A CR Touch / BLTouch is a nice upgrade |

**Suggested slicer settings (starting point):**
- 0.4 mm nozzle, 0.2 mm layers.
- **4–5 walls**, 5 top and 5 bottom layers, **30–40% gyroid infill**.
- No supports, no brim.
- Optional ironing on the top face.

Expect roughly **100–130 g of filament (~$2–3) and several hours per cartridge**. Your slicer will give the real time; a 0.6 mm nozzle cuts it a lot.

**What to look for in a borrowed printer:**
- An all-metal hotend (PETG/nylon).
- Textured PEI.
- Working pause-at-height.
- A multi-material system (e.g. Bambu AMS, Prusa MMU) if you want full-colour characters.

## 4. What a "print service" is, and whether you need one

A print service prints your STL for you and ships it. You upload the file, pick a material and colour, and pay per part.

| Option | What it is | Good for |
|---|---|---|
| **Local library or makerspace** | Many public libraries and makerspaces have printers you can use for the cost of filament | Free or cheap, and same week |
| **Craftcloud** | A price-comparison marketplace across many print shops | Seeing options and prices in one place |
| **JLC3DP** (JLCPCB), PCBWay | Large online print farms: FDM, resin, and industrial nylon (SLS/MJF) | Cheap industrial parts, typically 1–2 weeks shipping |
| **Xometry** and similar | Industrial on-demand manufacturing | Higher-end materials and finishes |

**Since you own an Ender 3 Pro, you don't need a service for prototyping.** A service is only worth it for
**premium nylon (MJF/SLS) cartridges**. Nylon is extremely tough and slightly flexible, which is great for a
toddler. But a service can't pause to embed the tag, so nylon means the two-halves design or pocket-plus-plug.

## 5. Experiments

1. **E1: NFC range.** Print `nfc_gap_steps`. With the PN532 flat on the desk, record reads at 5–30 mm with your tags.
   Pass: a reliable read at ≥ 25 mm, which gives margin over the 23 mm design gap.
2. **E2: Pause test.** Print one `cartridge_single_star` with a tag. It passes if the print resumes cleanly, the tag reads,
   and nothing is visible or peelable.
3. **E3: Slot fit and removal.** Print `slot_mockup`, strap the PN532 to its wall and run the daemon. Check:
   insert → play and remove → pause (NFC-only), how it feels to pull, and that it can't jam.
4. **E4: Durability.** Drop from ~1 m onto hardwood, stand on it (adult), and do a chew/grip check. PLA vs PETG.
5. **E5: Character design.** If E1–E4 pass, design a few characters, e.g. icon swaps or a sculpted topper on
   the 40 mm that sticks out.

**Decision gate:** if E2 and E4 pass in PETG, printed cartridges become the default and wood remains the "premium" option.
If not, keep wood blocks and use the printer for brackets, the LED pixel grid and the slot mock-up.

## 6. Regenerating the STLs

```bash
cd hardware/3d
openscad -o stl/cartridge_single_star.stl cartridge.scad
openscad -D 'mode="half"' -D 'half="a"' -o stl/cartridge_half_a.stl cartridge.scad
openscad -D 'mode="half"' -D 'half="b"' -o stl/cartridge_half_b.stl cartridge.scad
openscad -D 'mode="half"' -D 'half="pins"' -o stl/cartridge_pins.stl cartridge.scad
openscad -o stl/nfc_gap_steps.stl nfc_gap_steps.scad
openscad -o stl/slot_mockup.stl slot_mockup.scad
```
