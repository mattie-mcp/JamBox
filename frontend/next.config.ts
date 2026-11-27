import type { NextConfig } from "next";

// Built as plain static files (frontend/out) that FastAPI serves on the Pi.
// No Node.js runs on the box; build on a laptop or in CI and copy `out/` over.
const nextConfig: NextConfig = {
  output: "export",
};

export default nextConfig;
