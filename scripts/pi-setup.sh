#!/bin/bash
set -euo pipefail

echo "=== JamBox - Raspberry Pi Setup ==="

# System updates
echo "[1/5] Updating system..."
sudo apt update && sudo apt upgrade -y

# Install system dependencies
echo "[2/5] Installing dependencies..."
sudo apt install -y python3-pip python3-venv i2c-tools libusb-dev

# Enable I2C
echo "[3/5] Enabling I2C..."
sudo raspi-config nonint do_i2c 0

# Install Raspotify
echo "[4/5] Installing Raspotify..."
curl -sL https://dtcooper.github.io/raspotify/install.sh | sh

# Backend setup
echo "[5/5] Setting up backend..."
cd ~/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[pi]"

echo ""
echo "=== Setup complete! ==="
echo "Next steps:"
echo "  1. Copy .env.example to .env and add your Spotify credentials"
echo "  2. Start backend: cd backend && source .venv/bin/activate && uvicorn app.main:app --host 0.0.0.0"
echo "  3. Visit http://<pi-ip>:8000/auth/login to authenticate Spotify"
echo "  4. On your laptop, build and copy the parent UI: scripts/deploy-ui.sh"
echo "     (No Node on the Pi. The backend serves the UI at http://<pi-ip>:8000/)"
echo "  5. Start NFC daemon: cd backend && python -m app.nfc_daemon"
