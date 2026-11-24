// NFC read-range test: a stepped spacer.
// Lay the PN532 flat, set this on top with the tag on a chosen step, and record
// whether it reads. Each step is labelled with its thickness in mm.
// Prints flat, no supports. PLA is fine (plastic is NFC-transparent).
steps  = [5, 10, 15, 20, 25, 30];   // mm
step_w = 40;                         // each step is a 40 x 60 mm pad (fits a 35 mm tag)
depth  = 60;
$fn = 32;

// two rows of three so it fits a 220 x 220 mm bed (Ender 3): 120 x 120 mm overall
for (i = [0:len(steps) - 1]) {
    translate([(i % 3) * step_w, floor(i / 3) * depth, 0]) difference() {
        cube([step_w, depth, steps[i]]);
        translate([step_w / 2, 6, steps[i] - 0.6])
            linear_extrude(0.61) text(str(steps[i]), size = 7, halign = "center", font = "Liberation Sans:style=Bold");
        // tag outline target
        translate([step_w / 2, depth / 2 + 4, steps[i] - 0.4]) difference() {
            cylinder(d = 36, h = 0.41); cylinder(d = 34.4, h = 0.42);
        }
    }
}
