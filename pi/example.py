from signal import pause
from time import sleep

from gpiozero import Button, LED
from ADCDevice import *
from gpiozero import MotionSensor



disp_info = True
info_led = LED(18)


def show_info():
    info_led.on()
    sleep(0.1)
    info_led.off()
    sleep(0.1)
    info_led.on()
    sleep(0.1)
    info_led.off()


def send_data(data):
    print("send_data not implemented but ->", data)
    success = True

    if success and disp_info:
        show_info()
    return success


def setup(user_devices):
    devices = []
    for device in user_devices:
        devices.append(get_input_device(device))

    return devices


def get_input_device(device):
    pin = device["pin"]
    type_input = device["type_input"]
    fcn = device["fcn"]

    #  example for a button :
    #  just add the name of your function as a string in user_devices

    if type_input == "button":
        temp = Button(pin)
        temp.when_activated = eval(fcn)

    else:
        print(type_input, "in", pin, "not supported, add your pwn code for it or verify given information")
    #  CREATE YOU OWN DEVICES TO PLEASE YOUR NEEDS.

    return temp



def main():
    user_devices = [
        {"pin": "21", "type_input": "button", "fcn": "test"},
    ]

    devices = setup(user_devices)

    adc = PCF8591()  # -> setup()

    old_pot0 = adc.analogRead(0)
    old_pot1 = adc.analogRead(1)

    while True:
        pot0 = adc.analogRead(0)
        pot1 = adc.analogRead(1)

        if old_pot0 != pot0:
            old_pot0 = pot0
            send_data(str(pot0)+" # 0")

        if old_pot1 != pot1:
            old_pot1 = pot1
            send_data(str(pot1)+" # 1")

        sleep(0.1)


#USER'S FUNCTIONS HERE


def test():
    send_data("Button")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
