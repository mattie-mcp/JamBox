#!/bin/bash
# Build the parent web UI (static export) and copy it to the Pi.
# Run on your laptop, not the Pi. The Pi has no Node; FastAPI serves frontend/out.
# Run: scripts/deploy-ui.sh   (set PI_HOST to override pi-3b.local)

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PI_HOST="${PI_HOST:-pi-3b.local}"

echo "Building frontend..."
cd "$REPO_DIR/frontend"
npm ci
npm run build

echo "Copying UI to $PI_HOST..."
rsync -av --delete "$REPO_DIR/frontend/out/" "admin@$PI_HOST:/home/admin/src/JamBox/frontend/out/"

echo "Done. Parent UI: http://$PI_HOST:8000/"
