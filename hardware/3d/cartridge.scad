// JamBox cartridge, parametric (OpenSCAD)
//
// Printed lying flat: X = width, Y = height (in use), Z = thickness.
// The NFC tag is sealed INSIDE the print, so there is nothing to peel off.
//
// mode = "single": one print. Pause at TAG_PAUSE_Z (see echo output), drop the tag
//                  into the pocket, resume. The pocket is exactly tag-deep, so the
//                  next layer prints straight onto the tag with no bridging.
// mode = "half":   two halves glued face to face (for printers or slicers without
//                  a pause). The pocket is in the "a" half; two loose printed pins
//                  ("pins") align the halves. Both halves print glue-face down.
//
// Units: mm. See docs/plans/2026-11-24-3d-printed-cartridges.md

/* [Shape] */
mode      = "single";   // ["single", "half"]
half      = "a";        // ["a", "b", "pins"]  (mode = "half" only)
width     = 80;
height    = 100;
thick     = 30;
edge_r    = 6;          // roundover on every edge

/* [NFC tag] */
tag_d     = 35;         // tag diameter (NTAG215 coin or sticker)
tag_t     = 1.0;        // tag thickness: measure yours (stickers ~0.3, PVC coins ~0.8-1.0)
tag_clear = 0.6;        // diametral clearance
tag_y     = 33;         // tag centre, measured up from the cartridge bottom edge

/* [Artwork] */
icon      = "star";     // ["star", "heart", "circle", "note", "none"]
icon_size = 36;
icon_y    = 76;         // centre of icon, up from the bottom edge (the part that sticks out of the slot)
relief    = 1.2;        // icon height above the face; a filament change here gives a 2-colour icon
both_faces= true;       // "half" mode only: icon on both faces (single prints lie on their back face)

/* [Fit] */
pin_d     = 4;
pin_len   = 6;
pin_clear = 0.3;

$fn = 64;

// ---------- derived ----------
tag_center_z = thick / 2;
pocket_top_z = tag_center_z + tag_t / 2;
pocket_bot_z = tag_center_z - tag_t / 2;

echo(str("TAG_PAUSE_Z: pause the print at the first layer ABOVE z = ", pocket_top_z,
         " mm (insert tag, then resume)"));

module rounded_block(w, h, t, r) {
    hull() for (x = [r, w - r], y = [r, h - r], z = [r, t - r])
        translate([x, y, z]) sphere(r = r);
}

module star2d(s) {
    pts = [for (i = [0:9]) let(a = 90 + i * 36, rr = (i % 2 == 0) ? s / 2 : s / 4.6)
           [rr * cos(a), rr * sin(a)]];
    offset(r = 1.2) offset(delta = -1.2) polygon(pts);    // soften the points
}
module heart2d(s) {
    k = s / 30;
    scale([k, k]) offset(r = 1) union() {
        translate([-6.5, 3]) circle(r = 8);
        translate([6.5, 3]) circle(r = 8);
        polygon([[-14.6, 0], [14.6, 0], [0, -15]]);
    }
}
module note2d(s) {
    k = s / 30;
    scale([k, k]) union() {
        translate([-5, -9]) circle(r = 5.5);
        translate([-0.6, -10]) square([3, 22]);
        translate([-0.6, 9]) polygon([[0, 3], [3, 3], [11, -3], [11, -8], [3, -2]]);
    }
}
module icon2d() {
    if (icon == "star")   star2d(icon_size);
    if (icon == "heart")  heart2d(icon_size);
    if (icon == "circle") circle(d = icon_size * 0.8);
    if (icon == "note")   note2d(icon_size);
}

module tag_pocket() {
    translate([width / 2, tag_y, pocket_bot_z])
        cylinder(d = tag_d + tag_clear, h = tag_t + 0.01);
}

// Raised icons. top = the +Z face, bottom = the -Z face (mirrored so it reads correctly).
module icons(top = true, bottom = false) {
    if (icon != "none") {
        if (top)    translate([width / 2, icon_y, thick - 0.4]) linear_extrude(relief + 0.4) icon2d();
        if (bottom) translate([width / 2, icon_y, -relief]) linear_extrude(relief + 0.4) mirror([1, 0]) icon2d();
    }
}

// Single print: lies on its flat back face, so only the top face carries a raised icon.
module cartridge_single() {
    difference() {
        union() { rounded_block(width, height, thick, edge_r); icons(true, false); }
        tag_pocket();
    }
}

// Halves: both print GLUE-FACE DOWN, so each outer face (and its icon) is on top.
pin_xy = [[width * 0.22, height * 0.2], [width * 0.78, height * 0.8]];

module whole_with_icons() { union() { rounded_block(width, height, thick, edge_r); icons(true, both_faces); } }

module half_a() {   // the -Z half, holds the tag pocket and pin holes; flipped glue-face down
    translate([0, 0, thick / 2]) mirror([0, 0, 1]) difference() {
        intersection() {
            whole_with_icons();
            translate([-1, -1, -relief - 1]) cube([width + 2, height + 2, thick / 2 + relief + 1]);
        }
        translate([width / 2, tag_y, thick / 2 - tag_t]) cylinder(d = tag_d + tag_clear, h = tag_t + 0.01);
        for (p = pin_xy) translate([p[0], p[1], thick / 2 - pin_len / 2]) cylinder(d = pin_d + pin_clear, h = pin_len / 2 + 0.01);
    }
}
module half_b() {   // the +Z half; moved glue-face down, with matching pin holes
    translate([0, 0, -thick / 2]) difference() {
        intersection() {
            whole_with_icons();
            translate([-1, -1, thick / 2]) cube([width + 2, height + 2, thick / 2 + relief + 1]);
        }
        for (p = pin_xy) translate([p[0], p[1], thick / 2 - 0.01]) cylinder(d = pin_d + pin_clear, h = pin_len / 2 + 0.01);
    }
}
module pins() {     // two loose alignment pins, printed standing up
    for (i = [0:1]) translate([i * 10, 0, 0]) cylinder(d = pin_d, h = pin_len - 0.4);
}

if (mode == "single") cartridge_single();
else if (half == "a") half_a();
else if (half == "b") half_b();
else pins();
