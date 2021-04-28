# RaspiMote
# https://github.com/RaspiMote
# Copyright (C) 2021 RaspiMote (@A-delta & @Firmin-Launay)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

from . import configuration, running, USB_Devices, controller_devices, GPIO_inputs
from urllib3 import disable_warnings as urllib_disable_warnings
from os import getenv

urllib_disable_warnings()


class Pi(
    configuration.Mixin,
    running.Mixin,
    USB_Devices.Mixin,
    controller_devices.Mixin,
    GPIO_inputs.Mixin
):

    def __init__(self, ip, connection_mode, debug_inventory=False,verbose=False):  # user_supported_devices could be a json file
        """
        Creates a Pi object.

        :param ip: IP of the pc that runs the driver.
        :param connection_mode: "WifI" : Only WiFi is functional for the moment.
        :param verbose: for development purposes only.
        """

        self.term_header = '\033[95m'
        self.term_blue_ok = '\033[94m'
        self.term_cyan_ok = '\033[96m'
        self.term_ok_green = '\033[92m'
        self.term_warning = '\033[93m'
        self.term_fail = '\033[91m'
        self.term_endc = '\033[0m'
        self.term_bold = '\033[1m'

        self.verbose = verbose
        self.log(self.term_header + "Verbose enabled" + self.term_endc)
        self.debug_inventory = debug_inventory

        if connection_mode == "WiFi":
            self.connection_mode = connection_mode

        elif connection_mode == "BT":
            self.connection_mode = connection_mode
            print(self.term_fail, "Not supported connection mode", self.term_endc)
        else:
            print(self.term_fail, "Unknown connection mode", self.term_endc)

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

        self.display_info = False
        self.error_led = False
        self.success_led = False

        self.ADC = None
        self.ADC_channels = 0

        self.usb_devices = []
        self.usb_channels = []

        self.gamepads = []

        self.buttons = []
        self.pins = []

    def log(self, message, newline=True):
        if self.verbose:
            if newline:
                print(message)
            else:
                print(message, end='; ')
