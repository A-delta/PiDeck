# RaspiMote
# https://github.com/RaspiMote
# Copyright (C) 2021 RaspiMote (@A-delta & @Firmin-Launay)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.


from sys import platform
from os import system, path, chdir, getcwd, getenv, remove, _exit, mkdir
from requests import request
from random import randint
from json import dumps, load
import urllib3
import threading
import requests
import time
from inspect import currentframe, getframeinfo

urllib3.disable_warnings()


class Driver:
    def __init__(self, loop_connection=False, verbose=False):
        """
        Creates a Driver object.

        :param verbose: for development purposes only.
        """

        self.platform = platform
        self.driver_path = path.join(getcwd(), "driver")
        self.verbose = verbose
        self.loop_connection = loop_connection
        self.log(("Loop connection enabled",))

        self.code = str(randint(0, 9999999))
        self.ip = ''
        self.port = 9876

        self.load_config()

        self.log([self.platform, self.driver_path, self.code, self.ip, self.port])

    def log(self, messages):
        if self.verbose:
            for m in messages:
                print(m)

    def load_config(self):
        """
        Check for saved config.
        The first time, it will ask you for Pi's IP and save it in file.
        """

        if self.platform == "linux":

            self.config_file_path = f"{getenv('HOME')}/.config/RaspiMote/pi_ip.raspimote"
        elif self.platform == "win32":

            self.appdata_path = getenv('APPDATA')
            if not path.isdir(path.join(self.appdata_path, "RaspiMote")):
                mkdir(path.join(self.appdata_path, "RaspiMote"))

            self.appdata_path = path.join(self.appdata_path, "RaspiMote")
            self.config_file_path = path.join(self.appdata_path, "pi_ip.raspimote")

        if path.isfile(self.config_file_path):
            pi_ip = open(self.config_file_path, 'r')
            self.ip = load(pi_ip)["ip"]
            pi_ip.close()
        else:
            if self.platform == "linux":
                self.ip = input("Input Piʼs IP address (temporary): ")

            elif self.platform == "win32":
                system("powershell -Command \".\\driver\\dialogText.ps1 RaspiMote 'Raspberry Piʼs IP address:'\" > NUL")
                try:
                    with open(path.join(self.appdata_path, "tmp", "dialogTextOutput.txt"), 'r', encoding="utf-16") as dialogTextOutput:
                        self.ip = dialogTextOutput.read().replace('\n', '')
                    remove(path.join(self.appdata_path, "tmp", "dialogTextOutput.txt"))
                    self.log(self.ip)
                except FileNotFoundError:
                    print("Aborting process.")
                    _exit(1)

        with open(self.config_file_path, 'w') as pi_ip:
            pi_ip.write(dumps({"ip": self.ip, "code": self.code}))

    def new_ip(self):
        if self.platform == "linux":
            config_file_path = f"{getenv('HOME')}/.config/RaspiMote/pi_ip.raspimote"
            self.ip = input("Input Piʼs IP address (temporary): ")

        elif self.platform == "win32":
            config_file_path = f"{getenv('APPDATA')}\\RaspiMote\\pi_ip.raspimote"
            system("powershell -Command \".\\driver\\dialogText.ps1 RaspiMote 'Raspberry Piʼs IP address:'\" > NUL")
            try:
                with open(path.join(self.appdata_path, "tmp", "dialogTextOutput.txt"), 'r', encoding="utf-16") as dialogTextOutput:
                    self.ip = dialogTextOutput.read().replace('\n', '')
                remove(path.join(self.appdata_path, "tmp", "dialogTextOutput.txt"))
                self.log(self.ip)
            except FileNotFoundError:
                print("Aborting process.")
                _exit(1)

        with open(self.config_file_path, 'w') as pi_ip:
            pi_ip.write(dumps({"ip": self.ip, "code": self.code}))

        return_to_est = self.establish_connection()

        return return_to_est

    def establish_connection(self):
        """
        This method establish connection with the Raspberry Pi by sending it a request.

        :return:
        """

        url = f"https://{self.ip}:{self.port}/connect"
        content = {"code": self.code, "platform": platform}
        headers = {"Content-Type": "application/json"}
        content = dumps(content)

        if not self.loop_connection:
            for tries in range(10):
                try:
                    connection = request('POST', url, data=content, headers=headers, verify=False)
                    return connection.text == "True"
                except requests.exceptions.ConnectionError:
                    print(f"Connection to Pi failed [{tries+1}/10]")
                    time.sleep(1)

            print("The driver is unable to connect to your Pi.")
            print("Please verify that Pi is running his software and hasn't encountered any error.")
            print("Do you want to edit the Pi's IP address?")
            new_ip = input(f"Currently, the IP address saved is \"{self.ip}\".\n\n(Y/n)  ").lower()

            if new_ip == "y" or new_ip == "" or new_ip == "yes":
                return_to_main = self.new_ip()
                return return_to_main
            else:
                print("Aborting process.")
                _exit(1)

        else:
            while True:
                try:
                    connection = request('POST', url, data=content, headers=headers, verify=False)
                    return connection.text == "True"
                except requests.exceptions.ConnectionError:
                    print(f"Connection to Pi failed, retrying...")

    def watchdog(self):
        time.sleep(2)
        address = "https://localhost:"+str(self.port)
        while True:
            try:
                requests.post(address)
                time.sleep(3)
            except Exception:
                break

        print("Restarting driver server")
        self.run()
        return

    def run(self):
        """
        This make the driver listen to post request from the Raspberry Pi and process it.

        :return:
        """
        watchdog = threading.Thread(name="Server Watchdog", target=self.watchdog)

        chdir(path.join(self.driver_path, "lan_server"))

        if self.platform == "win32":
            if self.verbose:
                frameinfo = getframeinfo(currentframe())
                current_line = frameinfo.lineno + 3
                print(f"\nYou are currently running RaspiMote in verbose mode. Consequently, your local installation of Python (which must be accessible by calling \"python\") will be used instead of the embeddable version. Ensure that the modules \"Flask\" and \"Flask-Cors\", along with \"https\", our fork of \"Cheroot\" are installed on your local installation. You can find more informations on \"https://docs.raspimote.tk/\". If you desire to change this behavior, you can edit the line {current_line} of \"{frameinfo.filename}\".\n")
                system(f'python wsgi_https.py -v')
            else:
                system(f'"C:\\Program Files\\RaspiMote\\py\\pythonw.exe" wsgi_https.py')

        elif self.platform == "linux":
            vb_arg = ['', ' -v'][int(self.verbose)]
            system(f'/usr/bin/python3 wsgi_https.py{vb_arg}')

        elif self.platform == "darwin":
            print("System not supported for the moment.")

        else:
            print("System not supported.")

        watchdog.start()
