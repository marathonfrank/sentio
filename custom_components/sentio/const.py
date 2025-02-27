"""Constants for the sentio sauna integration."""

DOMAIN = "sentio"
VERSION = "0.0.18"
SIGNAL_UPDATE_SENTIO = "update_sentio"
MANUFACTURER = "Sentiotec"
DEVICE_NAME = "Sentio Pro Sauna Controller"

SERIAL_PORT = "serial_port"
DEFAULT_SERIAL_PORT = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AB0L1AC3-if00-port0"
BAUD_RATE = 57600

MIN_SET_TEMP = 30
MAX_SET_TEMP = 110

HUMIDITY_MODELS = ("B3", "C3", "C3I", "D3", "D3I")
