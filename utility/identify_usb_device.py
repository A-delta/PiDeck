# 2021 RaspiMote
# https://github.com/RaspiMote

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
