"""Generate docs/design/jam-radio-v2.html: revised Jam Radio drawings + parts list by store.
Geometry follows docs/enclosure.md ("Inside the radio", revised 2026-11-27). Units: mm."""
import re, sys, html
from pathlib import Path

ROOT = Path(sys.argv[1])
S = 2.0  # px per mm in drawings

WOOD = "#e9c99a"; WOOD_D = "#c99a5e"; EDGE = "#7a5a33"; DARK = "#3b2a1a"
AMBER = "#ffb020"; ORANGE = "#ff7a1a"; RED = "#e8381c"

def box(x, y, w, h, **kw):
    a = " ".join(f'{k.replace("_","-")}="{v}"' for k, v in kw.items())
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" {a}/>'

def circ(cx, cy, r, **kw):
    a = " ".join(f'{k.replace("_","-")}="{v}"' for k, v in kw.items())
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" {a}/>'

def text(x, y, t, size=9, anchor="middle", fill=DARK, weight="normal"):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{fill}" font-weight="{weight}">{html.escape(t)}</text>'

def dim_h(x1, x2, y, label):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" class="dim" marker-start="url(#a)" marker-end="url(#a)"/>'
            + text((x1 + x2) / 2, y - 3, label, 8, fill="#555"))

def dim_v(x, y1, y2, label):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" class="dim" marker-start="url(#a)" marker-end="url(#a)"/>'
            + f'<text x="{x-4}" y="{(y1+y2)/2}" font-size="8" fill="#555" text-anchor="middle" transform="rotate(-90 {x-4} {(y1+y2)/2})">{label}</text>')

DEFS = ('<defs><marker id="a" viewBox="0 0 6 6" refX="3" refY="3" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
        '<path d="M0,0 L6,3 L0,6 z" fill="#777"/></marker>'
        '<pattern id="ply" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#e2bf8c"/>'
        '<path d="M0,3 H6" stroke="#cfa66d" stroke-width="0.6"/></pattern>'
        '<radialGradient id="glow"><stop offset="0" stop-color="#fff2c0"/><stop offset="1" stop-color="#ffb020" stop-opacity="0"/></radialGradient>'
        '</defs>')

# EQ levels (rows lit out of 8) for the 5 bands, plus peak dots
EQ = [7, 5, 6, 4, 2]; PEAK = [8, 6, 7, 5, 3]

def led_color(row):  # row 0 = bottom
    return AMBER if row < 3 else ORANGE if row < 6 else RED

def front_view():
    W, H = 360, 200
    ox, oy = 40, 70  # margin; svg y = oy + (200 - z)
    Z = lambda z: oy + (H - z)
    p = [f'<svg viewBox="0 0 {W+80} {H+130}" class="dwg">', DEFS]
    # cartridge sticking out of the top (behind the front face, shown as ghost) and knob
    p.append(box(ox + 140, Z(240), 80, 40, fill="#d79b5c", stroke=EDGE, rx=6, opacity="0.9"))
    p.append(text(ox + 180, Z(222), "cartridge", 8, fill="#fff"))
    p.append(f'<path d="M{ox+276},{Z(200)} q0,-14 6,-18 h38 q6,4 6,18 z" fill="#e7c08a" stroke="{EDGE}"/>')
    p.append(f'<ellipse cx="{ox+301}" cy="{Z(219)}" rx="25" ry="9" fill="#efcf9c" stroke="{EDGE}"/>')
    p.append(text(ox + 301, Z(234), "maple knob", 8))
    # body
    p.append(box(ox, Z(200), W, H, fill=WOOD, stroke=EDGE, stroke_width=1.5, rx=10))
    # hidden chamber walls
    for x in (102, 108, 252, 258):
        p.append(f'<line x1="{ox+x}" y1="{Z(188)}" x2="{ox+x}" y2="{Z(12)}" stroke="#a27a48" stroke-dasharray="3 3" stroke-width="0.8"/>')
    # grilles: 84 mm circle of 6 mm holes on a 9 mm grid, plus a V-groove ring
    for cx in (57, 303):
        p.append(circ(ox + cx, Z(100), 50, fill="none", stroke=WOOD_D, stroke_width=1.4))
        p.append(circ(ox + cx, Z(100), 42, fill="#d8b47e", stroke="none"))
        for gx in range(-36, 37, 9):
            for gz in range(-36, 37, 9):
                if gx * gx + gz * gz <= 39 * 39:
                    p.append(circ(ox + cx + gx, Z(100 + gz), 3, fill="#2b2118"))
    # LED window: rect z 80–150 + segmental arch to 164
    x0, x1 = ox + 154, ox + 206
    r = (26 ** 2 + 14 ** 2) / (2 * 14)
    p.append(f'<path d="M{x0},{Z(80)} V{Z(150)} A{r},{r} 0 0 1 {x1},{Z(150)} V{Z(80)} Z" fill="#2a1a10" stroke="{EDGE}" stroke-width="2"/>')
    p.append(f'<path d="M{x0+1.5},{Z(80)+1.5} V{Z(150)} A{r},{r} 0 0 1 {x1-1.5},{Z(150)} V{Z(80)+1.5} Z" fill="url(#glow)" opacity="0.25"/>')
    for c in range(5):
        for row in range(8):
            cx = ox + 163 + c * 8.5; cz = 85.25 + row * 8.5
            lit = row < EQ[c]; peak = row == PEAK[c] - 1 and not lit
            col = led_color(row) if (lit or peak) else "#4a2e1c"
            p.append(box(cx - 3.4, Z(cz) - 3.4, 6.8, 6.8, rx=1.5, fill=col, opacity="1" if lit or peak else "0.6"))
    # buttons: Back blue, Play/Pause green, Skip yellow
    for x, col, lab in ((140, "#2f7fd8", "Back"), (180, "#3fae4a", "Play/Pause"), (220, "#f2c230", "Skip")):
        p.append(circ(ox + x, Z(48), 13.5, fill="#2b2118"))
        p.append(circ(ox + x, Z(48), 10.5, fill=col, stroke="#fff", stroke_width=1, opacity="0.92"))
        p.append(text(ox + x, Z(22), lab, 7.5))
    # feet
    for x in (25, 335):
        p.append(box(ox + x - 12, Z(0), 24, 10, fill="#333", rx=3))
    # dims
    p.append(dim_h(ox, ox + W, oy + H + 34, "360"))
    p.append(dim_v(ox - 14, Z(200), Z(0), "200"))
    p.append(dim_h(ox + 57, ox + 303, oy + H + 22, "246 driver centres"))
    p.append(dim_h(x0, x1, Z(80) + 12, "52"))
    p.append(text(ox + 180, Z(171), "52 × 84 arched window", 7.5))
    p.append(text(ox + W / 2, 14, "Front", 12, weight="bold"))
    p.append("</svg>")
    return "\n".join(p)

def top_view():
    W, D = 360, 170
    ox, oy = 40, 40
    Y = lambda y: oy + (D - y)  # front at the bottom
    p = [f'<svg viewBox="0 0 {W+80} {D+100}" class="dwg">', DEFS]
    p.append(box(ox, Y(170), W, D, fill=WOOD, stroke=EDGE, stroke_width=1.5, rx=10))
    for (x, w) in ((12, 96), (252, 96)):
        p.append(box(ox + x, Y(82), w, 70, fill="none", stroke="#a27a48", stroke_dasharray="3 3"))
    p.append(text(ox + 57, Y(44), "L chamber (below)", 7.5, fill="#7a5a33"))
    p.append(text(ox + 303, Y(44), "R chamber (below)", 7.5, fill="#7a5a33"))
    # HDPE insert (110 × 50 visible) and slot 84 × 32
    p.append(box(ox + 125, Y(110), 110, 50, fill="#f4f4ee", stroke="#999", rx=3))
    p.append(box(ox + 138, Y(101), 84, 32, fill="#2b2118", rx=2))
    p.append(box(ox + 140, Y(100), 80, 30, fill="#d79b5c", stroke=EDGE, rx=6))
    p.append(text(ox + 180, Y(83), "cartridge 80 × 30", 7.5, fill="#fff"))
    p.append(box(ox + 158, Y(110), 44, 6, fill="#2f7d4f", opacity="0.85"))
    p.append(text(ox + 180, Y(128), "PN532 (under, back wall)", 7, fill="#2f7d4f"))
    # knob
    p.append(circ(ox + 300, Y(120), 25.5, fill="#efcf9c", stroke=EDGE, stroke_width=1.2))
    p.append(circ(ox + 300, Y(120), 14, fill="none", stroke="#c99a5e"))
    p.append(text(ox + 300, Y(150), "knob Ø51", 7.5))
    p.append(dim_h(ox, ox + W, Y(0) + 24, "360"))
    p.append(dim_v(ox - 14, Y(170), Y(0), "170"))
    p.append(dim_h(ox + 138, ox + 222, Y(60) + 12, "slot 84"))
    p.append(text(ox + W / 2, Y(0) + 12, "front", 8, fill="#777"))
    p.append(text(ox + W / 2, 18, "Top", 12, weight="bold"))
    p.append("</svg>")
    return "\n".join(p)

def section_view():
    D, H = 170, 200
    ox, oy = 50, 70
    X = lambda y: ox + y; Z = lambda z: oy + (H - z)
    p = [f'<svg viewBox="0 0 {D+140} {H+120}" class="dwg">', DEFS]
    ply = dict(fill="url(#ply)", stroke=EDGE, stroke_width=0.8)
    # shell
    p.append(box(X(0), Z(200), 12, 200, **ply))      # front
    p.append(box(X(158), Z(200), 12, 200, **ply))    # back
    p.append(box(X(12), Z(12), 146, 12, **ply))      # bottom
    p.append(box(X(12), Z(200), 146, 12, **ply))     # top
    # service opening in back z 22–120 (gap) and cover
    p.append(box(X(158), Z(120), 12, 98, fill="#fff", stroke="none"))
    p.append(box(X(170), Z(130), 6, 118, fill="#d9b37c", stroke=EDGE, stroke_width=0.8))
    p.append(text(X(186), Z(75), "cover", 7, anchor="start"))
    # LED window opening in the front (z 80–164) + shield
    p.append(box(X(0), Z(164), 12, 84, fill="#2a1a10"))
    p.append(box(X(10.5), Z(164), 1.5, 84, fill=AMBER, opacity="0.7"))
    p.append(box(X(12), Z(150), 8, 70, fill="#5a3a22"))
    p.append(box(X(20), Z(152), 2, 74, fill="#1d5e8a"))
    p.append(text(X(24), Z(118), "LEDs", 7, anchor="start"))
    # button
    p.append(box(X(-3), Z(60), 3, 24, fill="#3fae4a"))
    p.append(box(X(12), Z(58), 33, 20, fill="#555", rx=2))
    p.append(text(X(30), Z(28), "button", 7))
    # rails, sled, Pi stack
    p.append(box(X(63), Z(22), 95, 10, fill=WOOD_D, stroke=EDGE, stroke_width=0.6))
    p.append(box(X(63), Z(28), 95, 6, **ply))
    p.append(box(X(80), Z(88), 60, 50, fill="#2f7d4f", opacity="0.85", rx=2))
    p.append(text(X(110), Z(60), "Pi 4 + Amp4", 7, fill="#fff"))
    p.append(text(X(110), Z(51), "+ proto HAT", 7, fill="#fff"))
    p.append(text(X(110), Z(16), "sled on rails", 7))
    # sleeve, insert, cartridge, PN532
    p.append(box(X(60), Z(200), 50, 12, fill="#f4f4ee", stroke="#999"))
    p.append(box(X(69), Z(200), 32, 12, fill="#fff"))
    p.append(box(X(63), Z(188), 6, 48, **ply)); p.append(box(X(101), Z(188), 6, 48, **ply))
    p.append(box(X(63), Z(140), 44, 6, **ply))
    p.append(box(X(69), Z(240), 32, 100, fill="#d79b5c", stroke=EDGE, rx=5))
    p.append(f'<line x1="{X(85)}" y1="{Z(240)}" x2="{X(85)}" y2="{Z(140)}" stroke="{EDGE}" stroke-dasharray="2 2" stroke-width="0.6"/>')
    p.append(box(X(83.5), Z(185.5), 3, 35, fill="#1d5e8a"))
    p.append(text(X(85), Z(246), "tag at centre", 7))
    p.append(box(X(104), Z(188.5), 3, 41, fill="#2f7d4f"))
    p.append(text(X(112), Z(176), "PN532", 7, anchor="start", fill="#2f7d4f"))
    p.append(text(X(112), Z(168), "18–20 mm gap", 7, anchor="start", fill="#2f7d4f"))
    # drain tube
    p.append(f'<path d="M{X(85)},{Z(134)} Q{X(120)},{Z(130)} {X(158)},{Z(126)} L{X(172)},{Z(126)}" fill="none" stroke="#6aa0c8" stroke-width="3" opacity="0.8"/>')
    p.append(text(X(130), Z(136), "drain", 7, fill="#4a7fa8"))
    # feet + air
    p.append(box(X(10), Z(0), 20, 10, fill="#333", rx=3)); p.append(box(X(140), Z(0), 20, 10, fill="#333", rx=3))
    p.append(f'<path d="M{X(100)},{Z(-6)} V{Z(10)}" stroke="#4a90d9" stroke-width="1.5" marker-end="url(#a)"/>')
    p.append(f'<path d="M{X(150)},{Z(150)} H{X(185)}" stroke="#d9534f" stroke-width="1.5" marker-end="url(#a)"/>')
    p.append(text(X(188), Z(147), "warm air out", 7, anchor="start", fill="#d9534f"))
    p.append(text(X(100), Z(-16), "cool air in", 7, fill="#4a90d9"))
    p.append(dim_h(X(0), X(170), Z(0) + 40, "170"))
    p.append(dim_v(X(0) - 16, Z(200), Z(0), "200"))
    p.append(text(ox + D / 2, 14, "Section through the slot", 12, weight="bold"))
    p.append("</svg>")
    return "\n".join(p)

def back_view():
    W, H = 360, 200
    ox, oy = 40, 30
    Z = lambda z: oy + (H - z)
    Xb = lambda x: ox + (W - x)  # seen from behind, mirrored
    p = [f'<svg viewBox="0 0 {W+80} {H+80}" class="dwg">', DEFS]
    p.append(box(ox, Z(200), W, H, fill=WOOD, stroke=EDGE, stroke_width=1.5, rx=10))
    p.append(box(ox + 40, Z(130), 280, 118, fill="#d9b37c", stroke=EDGE, rx=3))
    p.append(box(ox + 50, Z(120), 260, 98, fill="none", stroke="#a27a48", stroke_dasharray="3 3"))
    p.append(text(ox + 180, Z(75), "service cover (opening 260 × 98, sled slides out)", 8))
    for i in range(14):
        p.append(circ(ox + 70 + i * 17, Z(16), 2.6, fill="#2b2118"))
    p.append(text(ox + 180, Z(5) + 4, "inlet holes", 7, fill="#555"))
    for i in range(8):
        for j in range(3):
            p.append(circ(Xb(170) + i * 12 - 42, Z(152 + j * 12), 2.6, fill="#2b2118"))
    p.append(text(Xb(170) + 0, Z(190) + 2, "outlet vents", 7, fill="#555"))
    p.append(circ(Xb(180), Z(126), 4, fill="#2b2118"))
    p.append(circ(Xb(240), Z(165), 11, fill="#c99a5e")); p.append(box(Xb(240) - 5, Z(165) - 2, 10, 4, rx=2, fill="#222"))
    p.append(text(Xb(240), Z(146), "USB-C", 7))
    p.append(circ(Xb(290), Z(165), 11, fill="#c99a5e")); p.append(circ(Xb(290), Z(165), 9.5, fill="#ccc", stroke="#4aa3ff", stroke_width=1.5))
    p.append(text(Xb(290), Z(146), "power", 7))
    p.append(text(ox + W / 2, 14, "Back", 12, weight="bold"))
    p.append("</svg>")
    return "\n".join(p)

# ---- parts list from docs/shopping.md ----
md = (ROOT / "docs/shopping.md").read_text()
stores = {
    "1": ("PiShop.us", "https://www.pishop.us/cart.php"),
    "2": ("Adafruit", "https://www.adafruit.com/shopping_cart"),
    "3": ("Parts Express", "https://www.parts-express.com/cart"),
    "5": ("Mouser", "https://www.mouser.com/Cart/"),
    "6": ("Amazon", "https://www.amazon.com/gp/cart/view.html"),
    "7": ("McMaster-Carr", "https://www.mcmaster.com/order/"),
    "8": ("Woodcraft", "https://www.woodcraft.com/cart"),
}
notes = {
    "1": "Shipping at checkout",
    "2": "$57.97 with code OhFudge15; shipping at checkout",
    "3": "+ $9.95 shipping",
    "5": "+ $8.49 UPS Ground + $0.63 tariff",
    "6": "Free shipping (Prime). Your Scotch tape is also in this cart",
    "7": "Shipping at checkout",
    "8": "Free shipping over $50 (through Dec 1)",
}
sec = md[md.index("### Line items"):md.index("### Comparisons")]
rows = {}
for line in sec.splitlines():
    m = re.match(r"\| (\d) \| (.+?) \| (.+?) \| (\$[\d.]+) \| (.+?) \| (.+?) \| (.+?) \|$", line)
    if not m:
        continue
    cart, item, part, unit, qty, stock, link = m.groups()
    lm = re.search(r"\((https?://[^)]+)\)", link)
    rows.setdefault(cart, []).append((item, part, unit, qty, stock, lm.group(1) if lm else None))

def money(v): return float(v.replace("$", ""))
def qn(q):
    m = re.match(r"(\d+)", q); n = int(m.group(1)) if m else 1
    return n * (3 if "each" in q else 1)

parts_html = []
grand = 0.0
for cart in ("1", "2", "5", "6", "3", "7", "8"):
    name, url = stores[cart]
    items = rows.get(cart, [])
    sub = sum(money(u) * qn(q) for _, _, u, q, _, _ in items)
    grand += sub
    trs = []
    for item, part, unit, qty, stock, link in items:
        t = html.escape(item)
        if link:
            t = f'<a href="{link}">{t}</a>'
        trs.append(f"<tr><td>{t}</td><td class=mono>{html.escape(part)}</td><td class=num>{unit}</td><td class=num>{html.escape(qty)}</td><td>{html.escape(stock)}</td></tr>")
    parts_html.append(
        f'<section class="store"><h3><a href="{url}">{name}</a> <span class="sub">${sub:,.2f}</span></h3>'
        f'<p class="note">{notes[cart]}</p><table><thead><tr><th>Item</th><th>Part</th><th>Unit</th><th>Qty</th><th>Stock</th></tr></thead>'
        f'<tbody>{"".join(trs)}</tbody></table></section>')

still = """
<tr><td>Maple or cherry, ¾" (planed to 15 mm), ~3–4 bd-ft</td><td>Woodcraft of Grand Rapids or a local hardwood dealer</td><td>$30–50</td></tr>
<tr><td>Water-based toy-safe finish (EN 71-3 / ASTM F963)</td><td>Ask at Woodcraft of Grand Rapids</td><td>~$25–40</td></tr>
<tr><td>Perforated steel grille sheet, ~2–3 mm holes, 12 × 12"</td><td>Amazon</td><td>~$18</td></tr>
<tr><td>Maple veneer (0.6 mm) for the LED diffuser</td><td>Woodcraft</td><td>~$10</td></tr>
<tr><td>Handful of polyester fiberfill</td><td>Pillow or craft stash</td><td>$0–5</td></tr>
<tr><td>Router bits and Forstners, if not owned: ⅜" and ¼" roundover, 45° chamfer; 1-⅜", 15/16", ⅞" Forstner; 6 mm brad-point</td><td>Woodcraft</td><td>~$80–100</td></tr>
<tr><td><i>Optional:</i> Omron D2F-01L3 slot microswitch, only if the slot test fails</td><td>Mouser</td><td>~$3</td></tr>
"""

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Jam Radio v2: design and parts</title>
<style>
:root{{--ink:#2b2118;--muted:#6b5a48;--paper:#fbf6ee;--card:#fff;--line:#e6dccb;--accent:#c4621d}}
*{{box-sizing:border-box}}body{{margin:0;font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:var(--ink);background:var(--paper)}}
header{{padding:28px 32px 8px;max-width:1200px;margin:auto}}h1{{font-family:Georgia,serif;font-size:30px;margin:0 0 4px}}
.lede{{color:var(--muted);margin:0;max-width:820px}}main{{max-width:1200px;margin:auto;padding:0 32px 48px}}
h2{{font-family:Georgia,serif;font-size:22px;margin:32px 0 12px;border-bottom:2px solid var(--line);padding-bottom:6px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(460px,1fr));gap:18px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px}}
.dwg{{width:100%;height:auto;font-family:-apple-system,sans-serif}}.dim{{stroke:#888;stroke-width:.7}}
.keys{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:10px;margin:0;padding:0;list-style:none}}
.keys li{{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:8px;padding:8px 12px}}
.keys b{{display:block}}
.store{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin-bottom:16px}}
.store h3{{margin:0;font-size:18px;display:flex;justify-content:space-between}}.store h3 a{{color:var(--ink)}}
.sub{{font-variant-numeric:tabular-nums;color:var(--accent)}}.note{{margin:2px 0 8px;color:var(--muted);font-size:13px}}
table{{width:100%;border-collapse:collapse;font-size:13.5px}}th,td{{text-align:left;padding:5px 8px;border-top:1px solid var(--line);vertical-align:top}}
th{{color:var(--muted);font-weight:600;border-top:none}}td.num{{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}}
td.mono{{font-family:ui-monospace,Menlo,monospace;font-size:12px;white-space:nowrap}}a{{color:#9a4a12}}
.total{{font-size:18px;background:#fff3e0;border:1px solid #f0c48a;border-radius:10px;padding:12px 16px}}
@media (max-width:640px){{header,main{{padding-left:14px;padding-right:14px}}.grid{{grid-template-columns:1fr}}td.mono{{white-space:normal}}}}
</style></head><body>
<header><h1>Jam Radio v2: design and parts</h1>
<p class="lede">Revised 2026-11-27: no handle (it lives plugged into the wall), full-height speaker chambers, a 144 mm centre bay,
a centred 32 mm slot, sled on rails, power in the back panel, and the arched 5×8 LED dial. Drawn to scale (mm) from
<code>docs/enclosure.md</code>. The LEDs show the jukebox equaliser mid-song.</p></header>
<main>
<h2>Design</h2>
<div class="grid">
<div class="card">{front_view()}</div>
<div class="card">{top_view()}</div>
<div class="card">{section_view()}</div>
<div class="card">{back_view()}</div>
</div>
<h2>Key numbers</h2>
<ul class="keys">
<li><b>360 × 170 × 200 mm</b>12 mm Baltic birch, glued butt joints with glue blocks, 10 mm roundovers, 4 screw-on feet</li>
<li><b>Slot 32 × 84 mm</b>Stepped HDPE insert (two ¼" layers), 45° lip, no metal within 30 mm of the reader</li>
<li><b>Cartridge 80 × 100 × 30 mm</b>Two 15 mm maple halves, tag at the centre, ±0.5 mm</li>
<li><b>Read gap 18–20 mm</b>15 mm to the tag + 0–2 mm clearance + 3 mm pocketed wall</li>
<li><b>Chambers ≈ 1.0 L each</b>90 × 176 × 64 mm, sealed, drivers 246 mm apart behind 84 mm drilled grilles</li>
<li><b>Buttons 24 mm</b>Mini LED arcade buttons, 40 mm apart, nuts threadlocked; bay 144 mm</li>
<li><b>LED window 52 × 84 mm</b>Arch above the grid, maple veneer at the front face</li>
<li><b>Airflow ≈ 20 cm² in / out</b>Under the sled and low on the cover, out high on the back</li>
</ul>
<h2>Parts by store</h2>
{"".join(parts_html)}
<div class="total"><b>In carts: ${grand:,.2f}</b> of merchandise before shipping (≈ $583 with known shipping; ≈ $573 with the Adafruit code).
3D-printing supplies stay in Amazon's Saved for later. Nothing has been bought.</div>
<h2>Still to buy</h2>
<section class="store"><table><thead><tr><th>Item</th><th>Where</th><th>≈ Cost</th></tr></thead><tbody>{still}</tbody></table>
<p class="note">All-in estimate ≈ $789 (≈ $699 if you own the router bits and Forstners). You already have the PN532 reader, soldering kit, breadboard and jumpers.</p></section>
</main></body></html>"""

(ROOT / "docs/design/jam-radio-v2.html").write_text(page)
print("grand", round(grand, 2), {k: len(v) for k, v in rows.items()})
