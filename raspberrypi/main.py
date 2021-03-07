#!/usr/bin/env python3
# 2021 RaspiMote
# https://github.com/RaspiMote

from pi.pi import Pi
from sys import argv


def main(argv):
    if "-verbose" in argv or '-v' in argv:
        verbose = True
    else:
        verbose = False

    pi = Pi("192.168.1.16", "WiFi", verbose)
    pi.add_gamepad_device(0)
    pi.add_gamepad_device(2)
    pi.add_USB_Device(1, "mouse")
    pi.add_USB_Device(3, "num_pad")

    pi.establish_connection()


if __name__ == '__main__':
    try:
        main(argv)
    except KeyboardInterrupt:
        print("Program ended")
