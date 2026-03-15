#!/bin/bash
set -euo pipefail

echo "=== JamBox - Raspberry Pi Setup ==="

# System updates
echo "[1/6] Updating system..."
sudo apt update && sudo apt upgrade -y

# Install system dependencies
echo "[2/6] Installing dependencies..."
sudo apt install -y python3-pip python3-venv nodejs npm i2c-tools libusb-dev

# Enable I2C
echo "[3/6] Enabling I2C..."
sudo raspi-config nonint do_i2c 0

# Install Raspotify
echo "[4/6] Installing Raspotify..."
curl -sL https://dtcooper.github.io/raspotify/install.sh | sh

# Backend setup
echo "[5/6] Setting up backend..."
cd ~/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[pi]"

# Frontend build
echo "[6/6] Building frontend..."
cd ~/frontend
npm install
npm run build

echo ""
echo "=== Setup complete! ==="
echo "Next steps:"
echo "  1. Copy .env.example to .env and add your Spotify credentials"
echo "  2. Start backend: cd backend && source .venv/bin/activate && uvicorn app.main:app --host 0.0.0.0"
echo "  3. Visit http://<pi-ip>:8000/auth/login to authenticate Spotify"
echo "  4. Start frontend: cd frontend && npm start"
echo "  5. Start NFC daemon: cd backend && python -m app.nfc_daemon"
