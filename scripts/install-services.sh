#!/bin/bash
# Install and enable JamBox systemd services on the Pi
# Run: sudo bash install-services.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Installing JamBox services..."

# Copy service files
cp "$SCRIPT_DIR/music-box-api.service" /etc/systemd/system/
cp "$SCRIPT_DIR/music-box-nfc.service" /etc/systemd/system/
cp "$SCRIPT_DIR/music-box-web.service" /etc/systemd/system/

# Build frontend if not already built
echo "Building frontend..."
cd /home/admin/src/JamBox/frontend
NEXT_PUBLIC_API_URL=http://pi-3b.local:8000 npx next build

# Reload systemd and enable services
systemctl daemon-reload
systemctl enable music-box-api music-box-nfc music-box-web
systemctl restart music-box-api music-box-nfc music-box-web

echo ""
echo "JamBox services installed and started!"
echo "  API:      http://pi-3b.local:8000"
echo "  Frontend: http://pi-3b.local:3000"
echo ""
echo "Useful commands:"
echo "  sudo systemctl status music-box-api music-box-nfc music-box-web"
echo "  sudo journalctl -u music-box-nfc -f    # follow NFC daemon logs"
echo "  sudo journalctl -u music-box-api -f    # follow API logs"
