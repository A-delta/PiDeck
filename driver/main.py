#!/usr/bin/env python3
# RaspiMote
# https://github.com/RaspiMote
# Copyright (C) 2021 RaspiMote (@A-delta & @Firmin-Launay)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

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
