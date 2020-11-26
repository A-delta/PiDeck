from .user_custom_functions import *
from gpiozero import Button, LED
from time import sleep


class Pi:
    def __init__(self, config):

        self.setup(config)

    def setup(self, user_supported_devices):

        disp_info = True  # ADD CHOICE
        error_led = LED(18)
        success_led = LED(23)


        devices = []  # easy support for buttons that reads in <user_devices>
        for device in user_supported_devices:
            devices.append(self.get_input_device(device))

        return devices

    def get_input_device(self, device):
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

            return new

        # Here you can add support for a device to make it easier to setup (for json configuration files for example.

        else:
            print(type_input, "in", pin, "not supported, add your own code for it or verify given information")

    def show_info(self, success):
        if success:
            self.success_led.on()
            sleep(0.1)
            self.success_led.off()
            sleep(0.1)
            self.success_led.on()
            sleep(0.1)
            self.success_led.off()
        else:
            self.error_led.on()
            sleep(0.1)
            self.error_led.off()
            sleep(0.1)
            self.error_led.on()
            sleep(0.1)
            self.error_led.off()

