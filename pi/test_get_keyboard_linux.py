# 2020 Adelta
# https://github.com/A-delta

from evdev import InputDevice, categorize, ecodes
import evdev
from time import sleep

# MY keyboard : 7
# pavé numérique usb on pc : 22 ||| on pi : 1

device = InputDevice(f"/dev/input/event7")
cnt = 0
for event in device.read_loop():

    if event.type == ecodes.EV_KEY:
        print(ecodes.KEY[event.code])

