#!/usr/bin/env python3
# RaspiMote
# https://github.com/RaspiMote
# Copyright (C) 2021 RaspiMote (@A-delta & @Firmin-Launay)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.


from pi.pi import Pi
from sys import argv


def main(argv):

    verbose = "-verbose" in argv or '-v' in argv
    debug_inventory = "inventory" in argv or "-i" in argv

    pi = Pi("192.168.1.16", "WiFi", debug_inventory, verbose)
    pi.establish_connection()



if __name__ == '__main__':
    try:
        main(argv)
    except KeyboardInterrupt:
        print("Program ended")
