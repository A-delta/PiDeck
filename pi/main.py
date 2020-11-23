from signal import pause
from time import sleep

from gpiozero import Button, LED

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
    print("Not implemented")
    print(data)
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

    if type_input == "button":
        temp = Button(pin)
        temp.when_activated = eval(fcn)

    return temp



def main():
    pin = 21
    type_input = "button"
    fcn = "button_test_pressed"

    user_devices = [
        {"pin": pin, "type_input": type_input, "fcn": fcn},
    ]

    devices = setup(user_devices)

    pause()


def button_test_pressed():
    send_data(None)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass