# 2020 Adelta
# https://github.com/A-delta

from gpiozero import Button, LED
from time import sleep, time
import datetime
from signal import pause
import threading
import requests
import os
from subprocess import run, check_output
import json
import urllib3

urllib3.disable_warnings()

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'


class Pi:
    def __init__(self, config, verbose, connection_mode="WiFi"):  # user_supported_devices could be a json file

        self.verbose = verbose
        self.log(HEADER+"Verbose enabled"+ENDC)

        if connection_mode == "WiFi":
            self.connection_mode = connection_mode
        elif connection_mode == "BT":
            self.connection_mode = connection_mode
        else:
            print(FAIL, "Unknown connection mode", ENDC)

        self.log(self.connection_mode)


        self.config_folder = os.getenv('HOME') + "/.config/RaspiMote/"

        self.ip = "192.168.1.16"  # Get server request ip
        self.code = 0

        self.display_info = True  # NEED TO ADD CHOICE
        self.error_led = LED(18)
        self.success_led = LED(23)

        self.has_ADC = False
        self.ADC = None
        self.ADC_channels = 0

        self.has_USB = False
        self.USB = None
        self.USB_channels = []

        self.buttons = []
        self.pins = []
        for device in config:
            device, pin = self.get_input_device(device)
            self.buttons.append(device)
            self.pins.append(pin)



    def log(self, message, newline=True):
        if self.verbose:
            if newline:
                print(message)
            else:
                print(message, end='; ')

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
            self.log(WARNING + type_input + "in" + pin + "not supported, add your own code for it or verify given information" + ENDC)


    def establish_connection(self):

        if self.connection_mode == "WiFi":

            if self.verbose:
                log_level = "--log-level critical"
            else:
                log_level = ''

            self.log(f"{WARNING}Waiting for connection from pc{ENDC}")
            led = threading.Thread(name='Connection Blink LED', target=self.show_connection)
            led.start()

            old_cwd = os.getcwd()

            os.chdir(os.path.join("raspimote", "server_pi"))
            run(f"gunicorn  {log_level} --certfile cert.pem --keyfile key.pem --bind 0.0.0.0:9876 wsgi:app".split())
            os.chdir(old_cwd)

            with open(os.path.join(self.config_folder, "connection.raspimote"), 'r', encoding="utf-8") as f:
                self.code = json.loads(f.read())["code"]
                self.log("\n Connection code : " + HEADER+str(self.code)+ENDC)

            self.send_inventory()

        elif self.connection_mode == "BT":
            print(FAIL, "Bluetooth unsupported", ENDC)

    def send_inventory(self):

        inventory = {"GPIO_buttons": []}

        for b in self.buttons:
            pin = self.pins[self.buttons.index(b)]
            inventory["GPIO_buttons"].append(pin)

        if self.has_ADC:
            inventory.update({"ADC_channels": self.ADC_channels})

        request = {"code": self.code, "inventory": inventory}
        print(request)

        self.send_data(request)

    def add_ADC_Device_PCF8591(self, number_channels):
        """
        I have no idea of how to support other ADCDevice for the moment.
        :return:
        """
        from ADCDevice import PCF8591

        self.has_ADC = True
        self.log(f"ADC Device added with {number_channels} channels used")
        self.ADC = PCF8591()
        self.ADC_channels += (number_channels - 1)

        self.ADC_old_values = []
        for channel in range(self.ADC_channels + 1):
            self.ADC_old_values.append(int(self.ADC.analogRead(channel)))

    def add_USB_Device(self, input_number):
        from evdev import InputDevice

        self.USB = InputDevice(f"/dev/input/event{input_number}")
        self.USB_channels.append(input_number)
        cnt = 0

        self.log(f"USB Device added with input{input_number}")

        usb_device_thread = threading.Thread(name="USB Device Reading", target=self.usb_device_loop)
        usb_device_thread.start()

    def usb_device_loop(self):
        from evdev import categorize, ecodes

        for event in self.USB.read_loop():
            if event.type == ecodes.EV_KEY:
                self.send_data({
                    "code": self.code,

                    "request": {
                        "type": "USB", "pin": self.USB_channels[0],
                        "value": ecodes.KEY[event.code],
                        "extra": event.value
                    }

                })  # Need to add support for more USB Device at the same time

                self.log(categorize(event))

    def run(self):
        if self.has_ADC:
            idle = 0
            time_sleep = 0.15
            while True:

                for channel in range(self.ADC_channels + 1):
                    old = self.ADC_old_values[channel]
                    new = int(self.ADC.analogRead(channel))

                    if old not in [new-1, new, new+1]:

                        idle = 1
                        time_sleep = 0.1

                        self.ADC_old_values[channel] = new

                        new = int((new / 255) * 100)

                        if self.verbose:
                            print(f"ADC{channel} : {new}", end='; ')

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
        pin = self.pins[self.buttons.index(button)]
        self.log(f"Button{pin}")
        self.send_data({"code": self.code, "request": {"type": "button", "pin": pin, "value": 1}})

    def send_data(self, data):
        start = 0
        if self.verbose:
            start = time()

        success = self.send_request(data)

        if success:
            self.log(f"Sent. at {BOLD}{datetime.datetime.now().time()}{ENDC}")
            t = threading.Thread(name='Blink LED', target=self.show_success)
        else:
            self.log(f"{FAIL}Error. at {BOLD}{datetime.datetime.now().time()}{ENDC}")
            t = threading.Thread(name='Blink LED', target=self.show_error)

        t.start()

        self.log(f"Answered in {str(time()-start)} at {BOLD}{datetime.datetime.now().time()}{ENDC}\n")

        return

    def send_request(self, data):

        url = f'https://{self.ip}:9876/action'
        headers = {"Content-Type": "application/json"}
        content = json.dumps(data)

        r = requests.post(url, data=content, headers=headers, verify=False)

        return r.status_code == requests.codes.ok

