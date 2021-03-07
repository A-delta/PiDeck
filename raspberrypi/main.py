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

    pi.add_generic_USB_device(0, "mouseblue")
    pi.add_generic_USB_device(1, "numpad")

    pi.establish_connection()


if __name__ == '__main__':
    try:
        main(argv)
    except KeyboardInterrupt:
        print("Program ended")
