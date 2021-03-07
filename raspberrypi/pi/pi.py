# 2021 RaspiMote
# https://github.com/RaspiMote

from . import configuration, running, USB_Devices, controller_devices, ADC_Devices
from urllib3 import disable_warnings as urllib_disable_warnings
from os import getenv

urllib_disable_warnings()

class Pi(
    configuration.Mixin,
    running.Mixin,
    USB_Devices.Mixin,
    controller_devices.Mixin,
    ADC_Devices.Mixin
):

    def __init__(self, ip, connection_mode, verbose=False):  # user_supported_devices could be a json file
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
