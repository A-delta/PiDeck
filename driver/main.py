#!/usr/bin/env python3
# 2021 Adelta
# https://github.com/A-delta

from sys import argv
from driver.driver import Driver


def main(argv):
    if "-verbose" in argv or '-v' in argv:
        verbose = True
    else:
        verbose = False

    driver = Driver(verbose)
    driver.load_config()
    driver.establish_connection()
    driver.run()

if __name__ == "__main__":
    main(argv)