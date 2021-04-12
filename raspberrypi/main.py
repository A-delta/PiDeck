#!/usr/bin/env python3
# 2021 RaspiMote
# https://github.com/RaspiMote


from pi.pi import Pi
from sys import argv


def main(argv):
    
    verbose = "-verbose" in argv or '-v' in argv
    debug_inventory = "inventory" in argv or "i" in argv

    pi = Pi("192.168.1.16", "WiFi", debug_inventory, verbose)
    pi.add_USB_mouse(0)
    pi.establish_connection()



if __name__ == '__main__':
    try:
        main(argv)
    except KeyboardInterrupt:
        print("Program ended")
