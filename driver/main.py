#!/usr/bin/env python3
# 2021 RaspiMote
# https://github.com/RaspiMote

from sys import argv
from driver.driver import Driver


def main(argv):
    if "-verbose" in argv or "-v" in argv:
        verbose = True
    else:
        verbose = False

    if "-loop" in argv or "-l" in argv:
        loop_connection = True
    else:
        loop_connection = False

    driver = Driver(loop_connection, verbose)
    driver.load_config()
    driver.establish_connection()
    driver.run()


if __name__ == "__main__":
    main(argv)
