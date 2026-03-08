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

## GPIO Pinboard Map (Pi 3 B+)

Looking at the Pi with USB ports facing you, pin 1 is top-left.

```
                  +-----+-----+
         3.3V [*] |  1  |  2  | [.] 5V
  >>> SDA/GPIO2 [*] |  3  |  4  | [.] 5V
  >>> SCL/GPIO3 [*] |  5  |  6  | [*] GND <<<
       GPIO4  [.] |  7  |  8  | [.] GPIO14/TX
          GND [.] |  9  | 10  | [.] GPIO15/RX
      GPIO17  [.] | 11  | 12  | [.] GPIO18
      GPIO27  [.] | 13  | 14  | [.] GND
      GPIO22  [.] | 15  | 16  | [.] GPIO23
         3.3V [.] | 17  | 18  | [.] GPIO24
      GPIO10  [.] | 19  | 20  | [.] GND
       GPIO9  [.] | 21  | 22  | [.] GPIO25
      GPIO11  [.] | 23  | 24  | [.] GPIO8
          GND [.] | 25  | 26  | [.] GPIO7
       GPIO0  [.] | 27  | 28  | [.] GPIO1
       GPIO5  [.] | 29  | 30  | [.] GND
       GPIO6  [.] | 31  | 32  | [.] GPIO12
      GPIO13  [.] | 33  | 34  | [.] GND
      GPIO19  [.] | 35  | 36  | [.] GPIO16
      GPIO26  [.] | 37  | 38  | [.] GPIO20
          GND [.] | 39  | 40  | [.] GPIO21
                  +-----+-----+

  [*] = JamBox connection    [.] = unused
  >>> = PN532 wire
```

### JamBox Wiring Summary

```
  PN532           Pi Pin    Wire Color (suggested)
  ─────           ──────    ──────────────────────
  VCC  ──────────  1        Red    (3.3V power)
  SDA  ──────────  3        Blue   (I2C data)
  SCL  ──────────  5        Yellow (I2C clock)
  GND  ──────────  6        Black  (ground)
```

Only 4 wires needed. Keep them short to reduce noise on the I2C bus.

## Raspberry Pi Setup
1. Flash Raspberry Pi OS (64-bit, Lite) to SD card using Raspberry Pi Imager
2. Enable SSH and WiFi during imaging
3. Boot Pi, SSH in, run `sudo apt update && sudo apt upgrade -y`
4. Enable I2C: `sudo raspi-config` > Interface Options > I2C > Enable
5. Install Bluetooth: `sudo apt install -y bluetooth bluez`
6. Pair speaker: `bluetoothctl` > `scan on` > `pair <MAC>` > `connect <MAC>` > `trust <MAC>`
