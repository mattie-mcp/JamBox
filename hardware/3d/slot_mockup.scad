// Slot mock-up: the cartridge sleeve as a standalone print, for testing
// cartridge fit, the microswitch-free NFC-only removal detection, and PN532 placement
// before committing to the wooden box.
// Interior matches docs/enclosure.md: 34 x 84 mm opening, 60 mm deep, 45-degree lead-in.
inner_w = 84;   // along the cartridge width
inner_t = 34;   // along the cartridge thickness
depth   = 60;   // insertion depth
wall    = 6;    // same as the 6 mm plywood sleeve, so NFC tests are realistic
floor_t = 4;
lip     = 4;    // chamfer size at the opening
crumb_d = 12;   // clean-out hole in the floor
$fn = 48;

ow = inner_w + 2 * wall;
ot = inner_t + 2 * wall;
oh = depth + floor_t;

difference() {
    union() {
        cube([ow, ot, oh]);
        // flange so it sits flat on a desk / can be clamped
        translate([-15, -15, 0]) cube([ow + 30, ot + 30, 4]);
    }
    translate([wall, wall, floor_t]) cube([inner_w, inner_t, depth + 1]);
    // 45-degree lead-in chamfer
    translate([wall, wall, oh]) hull() {
        translate([0, 0, -lip]) cube([inner_w, inner_t, 0.01]);
        translate([-lip, -lip, 0]) cube([inner_w + 2 * lip, inner_t + 2 * lip, 0.01]);
    }
    translate([ow / 2, ot / 2, -1]) cylinder(d = crumb_d, h = floor_t + 2);
    // zip-tie slots on the back wall to strap a PN532 board against it
    for (x = [ow * 0.2, ow * 0.8], z = [floor_t + 10, floor_t + 45])
        translate([x - 2, -1, z]) cube([4, wall + 2, 3]);
}
