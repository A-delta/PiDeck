# 2020 Adelta
# https://github.com/A-delta

from evdev import InputDevice, categorize, ecodes
from time import sleep

# MY keyboard : 7
# pavé numérique usb : 22

device = InputDevice(f"/dev/input/event2")
cnt = 0
for event in device.read_loop():

    if event.type == ecodes.EV_KEY:

        print(categorize(event))

