#!/bin/bash
# Install and enable JamBox systemd services on the Pi
# Run: sudo bash install-services.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Installing JamBox services..."

# Copy service files
cp "$SCRIPT_DIR/jambox-api.service" /etc/systemd/system/
cp "$SCRIPT_DIR/jambox-nfc.service" /etc/systemd/system/
cp "$SCRIPT_DIR/jambox-web.service" /etc/systemd/system/

# Build frontend if not already built
echo "Building frontend..."
cd /home/admin/src/JamBox/frontend
NEXT_PUBLIC_API_URL=http://pi-3b.local:8000 npx next build

# Reload systemd and enable services
systemctl daemon-reload
systemctl enable jambox-api jambox-nfc jambox-web
systemctl restart jambox-api jambox-nfc jambox-web

echo ""
echo "JamBox services installed and started!"
echo "  API:      http://pi-3b.local:8000"
echo "  Frontend: http://pi-3b.local:3000"
echo ""
echo "Useful commands:"
echo "  sudo systemctl status jambox-api jambox-nfc jambox-web"
echo "  sudo journalctl -u jambox-nfc -f    # follow NFC daemon logs"
echo "  sudo journalctl -u jambox-api -f    # follow API logs"
