# Hardware Shopping List

## Required
| Item | Model | Approx Cost | Notes |
|------|-------|-------------|-------|
| Single-board computer | Raspberry Pi 3 Model B+ | $35 | 1GB RAM, BT 4.2, WiFi built in. Sufficient for prototype |
| NFC/RFID Reader | PN532 NFC Module | $10 | Supports I2C, SPI, and UART. Adafruit PN532 breakout recommended |
| NFC Tags | NTAG215 stickers (25 pack) | $12 | 13.56MHz, writable, good read range |
| MicroSD Card | 32GB+ Class 10 | $10 | For Pi OS |
| Power Supply | Micro-USB 5V/2.5A | $8 | Don't skimp on power supply |
| Jumper Wires | Female-to-female dupont wires | $5 | For connecting PN532 to Pi GPIO |
| Bluetooth Speaker | Any Bluetooth speaker | $0-30 | Use one you already own if possible |

**Total estimate: $80-110**

## Wiring: PN532 to Raspberry Pi (I2C mode)

| PN532 Pin | RPi Pin | RPi GPIO |
|-----------|---------|----------|
| VCC       | Pin 1   | 3.3V     |
| GND       | Pin 6   | Ground   |
| SDA       | Pin 3   | GPIO 2 (SDA) |
| SCL       | Pin 5   | GPIO 3 (SCL) |

Set PN532 DIP switches to I2C mode: Switch 1 = ON, Switch 2 = OFF

## Raspberry Pi Setup
1. Flash Raspberry Pi OS (64-bit, Lite) to SD card using Raspberry Pi Imager
2. Enable SSH and WiFi during imaging
3. Boot Pi, SSH in, run `sudo apt update && sudo apt upgrade -y`
4. Enable I2C: `sudo raspi-config` > Interface Options > I2C > Enable
5. Install Bluetooth: `sudo apt install -y bluetooth bluez`
6. Pair speaker: `bluetoothctl` > `scan on` > `pair <MAC>` > `connect <MAC>` > `trust <MAC>`
