# 2021 Adelta
# https://github.com/A-delta

from gpiozero import Button, LED
from signal import pause
from time import sleep, time
import datetime
from threading import Thread
from requests import post, codes, exceptions as requests_exceptions
from os import getenv, getcwd, chdir, path, system
from subprocess import run
from json import loads, dumps
from urllib3 import disable_warnings as urllib_disable_warnings, exceptions as urllib3_exceptions

urllib_disable_warnings()

term_header = '\033[95m'
term_blue_ok = '\033[94m'
term_cyan_ok = '\033[96m'
term_ok_green = '\033[92m'
term_warning = '\033[93m'
term_fail = '\033[91m'
term_endc = '\033[0m'
term_bold = '\033[1m'


"""note à moi-même : tous les 10min, tenter un ping au serveur, si pas de réponse, lancer establish_connection() de nouveau"""


class Pi:
    def __init__(self, ip, connection_mode, verbose=False):  # user_supported_devices could be a json file
        """
        Creates a Pi object.

        :param ip: IP of the pc that runs the driver.
        :param connection_mode: "WifI" : Only WiFi is functional for the moment.
        :param verbose: for development purposes only.
        """

        self.verbose = verbose

        self.log(term_header + "Verbose enabled" + term_endc)

        if connection_mode == "WiFi":
            self.connection_mode = connection_mode

        elif connection_mode == "BT":
            self.connection_mode = connection_mode
        else:
            print(term_fail, "Unknown connection mode", term_endc)

        self.log(self.connection_mode)

        self.ready = False
        self.config_folder = getenv('HOME') + "/.config/RaspiMote/"
        self.log(f"Config folder : {self.config_folder}")

        self.ip = ip
        self.driver_platform = ''
        self.log(f"Driver's IP : {ip}")

        self.code = 0
        self.server_url = f'{self.ip}:9876/action'
        self.request_headers = {"Content-Type": "application/json"}

        self.display_info = True  # NEED TO ADD CHOICE

        error_led_pin = 18
        success_led_pin = 23

        self.error_led = LED(18)
        self.success_led = LED(23)
        if self.display_info:
            self.log(f"Displaying infos on {error_led_pin} and {success_led_pin}")

        self.has_ADC = False
        self.ADC = None
        self.ADC_channels = 0

        self.has_USB = False
        self.usb_devices = []
        self.usb_channels = []

        self.has_gamepad = False
        self.gamepads = []

        self.buttons = []
        self.pins = []

    def add_buttons_configuration(self, config):
        """
        Add buttons configuration. You should run this methods only once.
        Only buttons type devices can be added with this method.

        :param config: list of dictionaries : [{"pin": "GPIO_PIN, "type_device": "button"}]
        :return:
        """
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
            self.log(term_warning + type_input + "in" + pin + "not supported, add your own code for it or verify given information" + term_endc)

    def establish_connection(self, timeout=False):
        """
        This method will make the Pi wait for a request from the driver.
        After receiving it, the driver will listen to post requests sent by the Raspberry Pi while reading inputs.
        This should the last line of your main file.

        :return:
        """

        if self.connection_mode == "WiFi":

            if self.verbose:
                log_level = ''
            else:
                log_level = "--log-level critical"

            if timeout:
                self.ready = False
                self.log(f"{term_fail}Timeout!{term_endc}")

            self.log(f"{term_warning}[WAITING] Connection from Driver{term_endc}")
            led = Thread(name='Connection Blink LED', target=self.show_connection)
            led.start()

            old_cwd = getcwd()

            chdir(path.join("raspimote", "server_pi"))
            run("/usr/bin/python3 wsgi_cheroot.py".split())
            chdir(old_cwd)

            with open(path.join(self.config_folder, "connection.raspimote"), 'r', encoding="utf-8") as f:
                content = loads(f.read())
                self.code = content["code"]
                self.driver_platform = content["platform"]
                self.log("\n Connection code : " + term_header + str(self.code) + term_endc)

            self.server_url = "https://" + self.server_url
            self.log(self.server_url)
            self.log(self.driver_platform)

            self.ready = True
            self.send_inventory()

            ping_thread = Thread(name="Ping server", target=self.ping_server)
            ping_thread.start()

            pause()

        elif self.connection_mode == "BT":
            print(term_fail, "Bluetooth unsupported", term_endc)

    def ping_server(self):
        while True:
            sleep(9)
            if self.verbose:
                run("vcgencmd measure_temp".split())

                start = time()

            content = dumps({"code": self.code, "request": {"type": "ping"}})
            try:
                response = post(self.server_url, data=content, headers=self.request_headers, verify=False)
                if self.verbose:
                    self.log(f"[PING] {term_ok_green}{str(time() - start)} s{term_endc}\n")
            except Exception as error:
                self.log(f"{term_fail}[FAIL] Retrying in 5s{term_endc}")
                sleep(5)
                try:
                    response = post(self.server_url, data=content, headers=self.request_headers, verify=False)
                except:
                    self.log(f"{term_fail}[FAIL] Restarting connection procedure{term_endc}")
                    break
        self.server_url = f'{self.ip}:9876/action'
        self.establish_connection()

    def send_inventory(self):
        inventory = {"GPIO_buttons": []}

        for b in self.buttons:
            pin = self.pins[self.buttons.index(b)]
            inventory["GPIO_buttons"].append(pin)

        if self.has_ADC:
            inventory.update({"ADC_channels": self.ADC_channels})

        if self.has_gamepad:
            for gp in self.gamepads:
                inventory.update({"gamepad": True})

        request = {"code": self.code, "request": {"type": "inventory", "inventory": inventory}}
        self.log(request)

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

        adc_device_thread = Thread(name="USB Device Reading", target=self.run_ADC)
        adc_device_thread.start()

    def add_USB_Device(self, input_number):
        """
        Add one or multiple USB devices, such as mouses (buttons) or keyboards.
        input_number can be found by running the provided script : /utility/identify_usb_device.py

        :param input_number: Number found by running the script. Also event number in /dev/input/ on UNIX systems.
        :return:
        """
        from evdev import InputDevice
        try:
            usb = InputDevice(f"/dev/input/event{input_number}")
        except:
            print(f"{term_fail}USB Device {input_number} doesn't exist. Skipped.{term_endc}")
            return
        self.usb_devices.append(usb)
        self.usb_channels.append(input_number)

        self.log(f"USB Device added with input{input_number}")

        usb_device_thread = Thread(name="USB Device Reading", target=self.usb_device_loop, args=(usb, input_number))
        usb_device_thread.start()




    def add_gamepad_device(self, input_number):
        from evdev import InputDevice

        try:
            gamepad = InputDevice(f"/dev/input/event{input_number}")
        except:
            print(f"{term_fail}Gamepad {input_number} doesn't exist. Skipped. Please verify number or Gamepad connection.{term_endc}")
            return
        self.gamepads.append(gamepad)
        self.has_gamepad = True



        gamepad_device_thread = Thread(name="Gamepad Device Reading", target=self.gamepad_device_loop, args=(gamepad, input_number))
        gamepad_device_thread.start()

    def gamepad_device_loop(self, gamepad, input_number):
        from evdev import categorize, ecodes

        CENTER_TOLERANCE = 350
        STICK_MAX = 65536

        axis = {
            ecodes.ABS_X: 'ls_x',  # 0 - 65,536   the middle is 32768
            ecodes.ABS_Y: 'ls_y',
            ecodes.ABS_Z: 'rs_x',
            ecodes.ABS_RZ: 'rs_y',
            ecodes.ABS_BRAKE: 'lt',  # 0 - 1023
            ecodes.ABS_GAS: 'rt',

            ecodes.ABS_HAT0X: 'dpad_x',  # -1 - 1
            ecodes.ABS_HAT0Y: 'dpad_y'
        }

        center = {
            'ls_x': STICK_MAX / 2,
            'ls_y': STICK_MAX / 2,
            'rs_x': STICK_MAX / 2,
            'rs_y': STICK_MAX / 2
        }


        for event in gamepad.read_loop():
            print(categorize(event))

            if event.type == ecodes.EV_KEY:
                print(categorize(event).keycode[0])
                button_name = categorize(event).keycode[0]

            elif event.type == ecodes.EV_ABS:
                print(event.code)
                if axis[event.code] in ['ls_x', 'ls_y', 'rs_x', 'rs_y']:
                    button_name = axis[event.code]
                    value = event.value - center[axis[event.code]]

                    if abs(value) <= CENTER_TOLERANCE:
                        value = 0

            self.send_data({
                "code": self.code,
                "request": {
                    "type": "controller",
                    "pin": input_number,
                    "value": button_name,
                    "extra": value

                }
            })















    def usb_device_loop(self, usb, input_number):
        from evdev import categorize, ecodes

        for event in usb.read_loop():
            if event.type == ecodes.EV_KEY:
                self.send_data({
                    "code": self.code,

                    "request": {
                        "type": "USB",
                        "pin": input_number,
                        "value": ecodes.KEY[event.code],
                        "extra": event.value
                    }

                })

                self.log(categorize(event))

    def run_ADC(self):
        if not self.has_ADC:
            print("NO ADC")  # need to clean errors
        else:
            idle = 0
            time_sleep = 0.15
            while True:
                for channel in range(self.ADC_channels + 1):
                    old = self.ADC_old_values[channel]
                    new = int(self.ADC.analogRead(channel))

                    if old not in [new - 1, new, new + 1]:

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

        r = Thread(name='Request', target=self.send_request, args=[data])
        r.start()

    def send_request(self, data):
        if not self.ready:
            self.log(f"{term_fail}Error. Request not sent : program not ready.{term_endc}")
            t = Thread(name='Blink LED', target=self.show_error)
            t.start()
            return

        if self.verbose:
            start = time()
        else:
            start = 0

        content = dumps(data)

        try:
            r = post(self.server_url, data=content, headers=self.request_headers, verify=False)
        except:
            print(f"{term_fail}Server not responding, driver might have stopped or encountered error{term_endc}")
            self.log(f"{term_fail}Error. at {term_bold}{datetime.datetime.now().time()}{term_endc}")
            error_LED_thread = Thread(name='Blink LED', target=self.show_error)
            error_LED_thread.start()
            # self.reconnect()
            return

        if r.status_code == codes.ok:
            self.log(f"Sent. at {term_bold}{datetime.datetime.now().time()}{term_endc}")
            info_LED_thread = Thread(name='Blink LED', target=self.show_success)
        else:
            self.log(f"{term_fail}Error. at {term_bold}{datetime.datetime.now().time()}{term_endc}")
            info_LED_thread = Thread(name='Blink LED', target=self.show_error)

        self.log(f"Answered in {str(time() - start)} at {term_bold}{datetime.datetime.now().time()}{term_endc}\n")
        info_LED_thread.start()

