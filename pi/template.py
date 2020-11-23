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
    print("send_data not implemented")
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
    user_devices = []
    """user_devices = [
        {"pin": "21", "input_type": "button", "fcn": "test"},
    ]"""

    devices = setup(user_devices)

    pause()



#USER'S FUNCTIONS HERE


def button_test_pressed2():
    print("2")
    send_data(None)


def button_test_pressed():
    print("1")
    send_data(None)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
