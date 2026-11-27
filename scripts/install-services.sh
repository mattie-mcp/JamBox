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

# Remove the old Next.js frontend service (the API now serves the UI)
if [ -f /etc/systemd/system/jambox-web.service ]; then
    echo "Removing old jambox-web service..."
    systemctl stop jambox-web || true
    systemctl disable jambox-web || true
    rm -f /etc/systemd/system/jambox-web.service
fi

# Install user service for Spotify Connect (runs as admin, not root)
USER_SERVICES="$ADMIN_HOME/.config/systemd/user"
mkdir -p "$USER_SERVICES"
cp "$SCRIPT_DIR/jambox-spotify.service" "$USER_SERVICES/"
chown -R admin:admin "$ADMIN_HOME/.config/systemd"

# Enable lingering so user services start at boot (not just on login)
loginctl enable-linger admin

# Reload and enable system services
systemctl daemon-reload
systemctl enable jambox-api jambox-nfc
systemctl restart jambox-api jambox-nfc

# Enable and start user service (as admin)
sudo -u admin XDG_RUNTIME_DIR="/run/user/$(id -u admin)" systemctl --user daemon-reload
sudo -u admin XDG_RUNTIME_DIR="/run/user/$(id -u admin)" systemctl --user enable jambox-spotify
sudo -u admin XDG_RUNTIME_DIR="/run/user/$(id -u admin)" systemctl --user restart jambox-spotify

echo ""
echo "JamBox services installed and started!"
echo "  Parent UI and API: http://pi-3b.local:8000/"
echo "  (Build the UI on your laptop and copy it over with scripts/deploy-ui.sh)"
echo "  Spotify:  running as user service (librespot)"
echo ""
echo "Useful commands:"
echo "  sudo systemctl status jambox-api jambox-nfc"
echo "  systemctl --user status jambox-spotify    # as admin user"
echo "  sudo journalctl -u jambox-nfc -f          # follow NFC daemon logs"
echo "  sudo journalctl -u jambox-api -f          # follow API logs"
echo "  journalctl --user -u jambox-spotify -f    # follow Spotify logs"
