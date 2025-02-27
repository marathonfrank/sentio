# Sentio integration for Home Assistant
[![Sentio](https://img.shields.io/github/v/release/astrandb/sentio)](https://github.com/astrandb/sentio/releases/latest) [![hacs_badge](https://img.shields.io/badge/HACS-Default-blue.svg)](https://github.com/custom-components/hacs)  [![Downloads for latest release](https://img.shields.io/github/downloads-pre/astrandb/sentio/latest/total.svg)](https://github.com/astrandb/sentio/releases/latest)

Custom component for Sentiotec sauna controller for integration in  Home Assistant
Changed ttyport: /dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AB0L1AC3-if00-port0
Changed Const for B3

## Preparation
In order to connect the Sentio Pro sauna controller you need a serial port with RS-485 interface on the server running Home Assistant. On Linux based machines the serial port is typically called /dev/ttyUSB0.

The user running Homeassistant should be added to group dialout - not needed if user is root.

## Installation
### Install with HACS (Recommended)
Search for Sentio integration and install it directly from HACS. HACS will keep track of updates and you can easily upgrade to latest version.

Restart Home Assistant

HACS can be found [here](https://hacs.xyz/)
### Install manually
If you want to install manually, you probably already know how to proceed.
## Configuration
Goto Settings->Integrations and press (+ Add integration)

Search for Sentio

Enter the port to use. On Linux typically /dev/ttyUSB0 .

Relevant entities will be created in HA depending on what the connected controller model supports

## Known limitations

The representation is varying for different Sentio Pro models. The support is fairly complete for models C2, C3, D2 & D3. If you miss any features, please create an issue here.

## Links
[Documentation](https://github.com/astrandb/sentio/wiki)
