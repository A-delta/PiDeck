from gpiozero import Button, LED
from os import getcwd, chdir, path
from json import loads
from signal import pause
from threading import Thread
from subprocess import run


class Mixin:
    def display_info(self, error_led_pin, success_led_pin):
        self.error_led = LED(error_led_pin)
        self.success_led = LED(success_led_pin)
        if self.display_info:
            self.log(f"Displaying infos on {error_led_pin} and {success_led_pin}")

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
                self.log(f"{self.term_fail}Timeout!{self.term_endc}")

            self.log(f"{self.term_warning}[WAITING] Connection from Driver{self.term_endc}")

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
                self.log("\n Connection code : " + self.term_header + str(self.code) + self.term_endc)

            self.server_url = "https://" + self.server_url
            self.log(self.server_url)
            self.log(self.driver_platform)

            self.ready = True
            self.send_inventory()

            ping_thread = Thread(name="Ping server", target=self.ping_server)
            ping_thread.start()

            pause()

        elif self.connection_mode == "BT":
            print(self.term_fail, "Bluetooth unsupported", self.term_endc)


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
