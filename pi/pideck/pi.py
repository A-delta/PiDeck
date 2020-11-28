from gpiozero import Button, LED
from time import sleep, time
from signal import pause
import threading
import requests
import os
from subprocess import run, check_output
import json
import logging

logging.getLogger("urllib3").setLevel(logging.WARNING)


class Pi:
    def __init__(self, config, verbose):  # user_supported_devices could be a json file

        self.verbose = verbose

        self.config_folder = os.getenv('HOME') + "/.config/PiDeck/"

        self.ip = "192.168.1.16"
        self.code = 0

        self.disp_info = True  # NEED TO ADD CHOICE
        self.error_led = LED(18)
        self.success_led = LED(23)

        self.establish_connection()

        self.ADC_channels = 0

        self.devices = []
        self.pins = []
        for device in config:
            device, pin = self.get_input_device(device)
            self.devices.append(device)
            self.pins.append(pin)


    def log(self, message):
        if self.verbose:
            print(message)

    def get_input_device(self, device):
        """
        This function is designed to handle multiple devices, there's only one for the moment.
        :param device:
        :return:
        """


        pin = device["pin"]
        type_input = device["type_input"]

        self.log(f"Configuring : GPIO{pin}, {type_input}")

        if type_input == "button":
            new = Button(pin)
            new.when_activated = self.event_button

            return new, pin

        # Here you can add support for a device to make it easier to setup (for json configuration files for example.

        else:
            self.log(type_input, "in", pin, "not supported, add your own code for it or verify given information")


    def establish_connection(self):
        self.log("Waiting for connection from pc")
        led = threading.Thread(name='Connection Blink LED', target=self.show_connection)
        led.start()

        old_cwd = os.getcwd()

        os.chdir(os.path.join("pideck", "server_pi"))
        run("gunicorn --certfile cert.pem --keyfile key.pem --bind 0.0.0.0:9876 wsgi:app".split())
        os.chdir(old_cwd)

        with open(os.path.join(self.config_folder, "connection.pideck"), 'r', encoding="utf-8") as f:
            self.code = json.loads(f.read())["code"]
            self.log(self.code)





    def add_ADC_Device_PCF8591(self, number_channels):
        """
        I have no idea of how to support other ADCDevice for the moment.
        :return:
        """
        from ADCDevice import PCF8591
        self.log(f"ADC Device added with {number_channels} channels used")
        self.ADC = PCF8591()
        self.ADC_channels += (number_channels - 1)

        self.ADC_old_values = []
        for channel in range(self.ADC_channels + 1):
            self.ADC_old_values.append(int((self.ADC.analogRead(channel)/255)*100))


    def run(self):
        adc = False
        try:
            if self.ADC != None:
                adc = True
        except:
            pass

        if adc:
            idle = 0
            time_sleep = 0.15
            while True:

                for channel in range(self.ADC_channels + 1):
                    old = self.ADC_old_values[channel]
                    new = int((self.ADC.analogRead(channel)/255)*100)

                    if old != new:

                        idle = 1
                        time_sleep = 0.075

                        self.ADC_old_values[channel] = new
                        self.send_data({"code": self.code, "request": {"type": "ADC", "pin": channel, "value": new}})

                    elif idle != 0:
                        idle += 1
                        if idle > 100:
                            self.log("Sleep mode")
                            time_sleep = 0.2
                            idle = 0
        else:
            pause()


    def show_connection(self):
        for _ in range(3):
            self.success_led.on()
            sleep(0.1)
            self.success_led.off()
            self.error_led.on()
            sleep(0.1)
            self.error_led.off()


    def show_success(self):
        self.success_led.on()
        sleep(0.1)
        self.success_led.off()
        sleep(0.1)
        self.success_led.on()
        sleep(0.1)
        self.success_led.off()

    def show_error(self):
        self.error_led.on()
        sleep(0.1)
        self.error_led.off()
        sleep(0.1)
        self.error_led.on()
        sleep(0.1)
        self.error_led.off()



    def event_button(self, button):
        pin = self.pins[self.devices.index(button)]
        self.log(pin)
        self.send_data({"code": self.code, "request": {"type": "button", "pin": pin, "value": 1}})

    def send_data(self, data):
        success = self.send_request(data)

        if success:
            t = threading.Thread(name='Blink LED', target=self.show_success)
        else:
            t = threading.Thread(name='Blink LED', target=self.show_error)

        t.start()
        return

    def send_request(self, data):

        url = f'https://{self.ip}:9876/action'
        headers = {"Content-Type": "application/json"}
        content = json.dumps(data)

        r = requests.post(url, data=content, headers=headers, verify=False)

        return r.status_code == requests.codes.ok

