from gpiozero import LED
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

    def establish_connection(self, timeout=False):
        """
        This method will make the Pi wait for a request from the driver.
        After receiving it, the driver will listen to post requests sent by the Raspberry Pi while reading inputs.
        This should the last line of your main file.

        :return:
        """

        if self.connection_mode == "WiFi":

            if self.verbose:
                log_level = ' -v'
            else:
                log_level = ''

            if timeout:
                self.ready = False
                self.log(f"{self.term_fail}Timeout!{self.term_endc}")

            self.log(f"{self.term_warning}[WAITING] Connection from Driver{self.term_endc}")

            led = Thread(name='Connection Blink LED', target=self.show_connection)
            led.start()

            old_cwd = getcwd()

            chdir(path.join("pi", "server_pi"))
            run(f"/usr/bin/python3 wsgi_https.py{log_level}".split())
            chdir(old_cwd)

            with open(path.join(self.config_folder, "connection.pi"), 'r', encoding="utf-8") as f:
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

        if self.ADC_channels != 0:
            inventory.update({"ADC_channels": self.ADC_channels})

        if self.usb_devices:
            inventory.update({"USB": self.usb_devices})

        if self.gamepads:
            inventory.update({"gamepad": len(self.gamepads)})

        if debug_inventory:
            inventory = {"GPIO_buttons": [2, 3, 4], "ADC": 12, "USB": ["mouse_0", "keyboard_0", "mouse_1", "generic_usb_0"], "gamepad": 1}


        request = {"code": self.code, "request": {"type": "inventory", "inventory": inventory}}
        self.log(request)

        self.send_data(request)
