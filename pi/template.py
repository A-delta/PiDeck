from signal import pause
from time import sleep

from gpiozero import Button, LED
from ADCDevice import *
from gpiozero import MotionSensor



disp_info = True
error_led = LED(18)
success_led = LED(23)
def testLED():
    while True:
        success_led.on()
        sleep(0.1)
        success_led.off()
        sleep(0.1)
        success_led.on()
        sleep(0.1)
        success_led.off()

        sleep(1)

        error_led.on()
        sleep(0.1)
        error_led.off()
        sleep(0.1)
        error_led.on()
        sleep(0.1)
        error_led.off()

        sleep(1)

def show_info(success):
    for _ in range(2):
        if success:
            success_led.on()
            sleep(0.1)
            success_led.off()
            sleep(0.1)
        else:
            error_led.on()
            sleep(0.1)
            error_led.off()
            sleep(0.1)


def send_data(data):
    print("send_data not implemented but ->", data)
    success = True

    if success and disp_info:
        show_info(True)
    return success


def setup(user_devices):
    """
    Put all your setup code here.
    Mine contains buttons and potentiometers.
    :param user_devices:
    :return:
    """

    devices = []  # easy support for buttons that reads in <user_devices>
    for device in user_devices:
        devices.append(get_input_device(device))

    return devices


def get_input_device(device):
    """
    This function is designed to handle multiple devices, there's only one for the moment.
    :param device:
    :return:
    """
    pin = device["pin"]
    type_input = device["type_input"]
    fcn = device["fcn"]

    if type_input == "button":
        new = Button(pin)
        new.when_activated = eval(fcn)

# Here you can add support for a device to make it easier to setup (for json configuration files for example.

    else:
        print(type_input, "in", pin, "not supported, add your own code for it or verify given information")

    return new



def main():
    user_devices = []

    devices = setup(user_devices)

    pause()



#USER'S FUNCTIONS HERE


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
