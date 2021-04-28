# RaspiMote
# https://github.com/RaspiMote
# Copyright (C) 2021 RaspiMote (@A-delta & @Firmin-Launay)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

from os import chdir, listdir
from threading import Thread
from evdev import InputDevice, ecodes


def find_device(event_number):
    device = InputDevice(f"/dev/input/{event_number}")
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            print(f"/dev/input/{event_number}")


def main():
    chdir("/dev/input")
    devices = []
    for e in listdir():
        if "event" in e:
            devices.append(e)

    for d in devices:
        t = Thread(target=find_device, args=[d])
        t.start()


if __name__ == "__main__":
    print("This script needs to run on your Raspberry Pi, hit any button of the target USB device ")
    main()
