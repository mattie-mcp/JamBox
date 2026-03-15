#!/bin/bash
# Install and enable JamBox systemd services on the Pi
# Run: sudo bash install-services.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ADMIN_HOME="/home/admin"

echo "Installing JamBox services..."

# Disable system Raspotify service (we run librespot as user instead)
if systemctl is-enabled raspotify &>/dev/null; then
    echo "Disabling system raspotify service..."
    systemctl stop raspotify
    systemctl disable raspotify
fi

# Copy system service files
cp "$SCRIPT_DIR/jambox-api.service" /etc/systemd/system/
cp "$SCRIPT_DIR/jambox-nfc.service" /etc/systemd/system/
cp "$SCRIPT_DIR/jambox-web.service" /etc/systemd/system/

# Install user service for Spotify Connect (runs as admin, not root)
USER_SERVICES="$ADMIN_HOME/.config/systemd/user"
mkdir -p "$USER_SERVICES"
cp "$SCRIPT_DIR/jambox-spotify.service" "$USER_SERVICES/"
chown -R admin:admin "$ADMIN_HOME/.config/systemd"

# Enable lingering so user services start at boot (not just on login)
loginctl enable-linger admin

# Build frontend if not already built
echo "Building frontend..."
cd "$ADMIN_HOME/src/JamBox/frontend"
sudo -u admin NEXT_PUBLIC_API_URL=http://pi-3b.local:8000 npx next build

# Reload and enable system services
systemctl daemon-reload
systemctl enable jambox-api jambox-nfc jambox-web
systemctl restart jambox-api jambox-nfc jambox-web

# Enable and start user service (as admin)
sudo -u admin XDG_RUNTIME_DIR="/run/user/$(id -u admin)" systemctl --user daemon-reload
sudo -u admin XDG_RUNTIME_DIR="/run/user/$(id -u admin)" systemctl --user enable jambox-spotify
sudo -u admin XDG_RUNTIME_DIR="/run/user/$(id -u admin)" systemctl --user restart jambox-spotify

echo ""
echo "JamBox services installed and started!"
echo "  API:      http://pi-3b.local:8000"
echo "  Frontend: http://pi-3b.local:3000"
echo "  Spotify:  running as user service (librespot)"
echo ""
echo "Useful commands:"
echo "  sudo systemctl status jambox-api jambox-nfc jambox-web"
echo "  systemctl --user status jambox-spotify    # as admin user"
echo "  sudo journalctl -u jambox-nfc -f          # follow NFC daemon logs"
echo "  sudo journalctl -u jambox-api -f          # follow API logs"
echo "  journalctl --user -u jambox-spotify -f    # follow Spotify logs"
