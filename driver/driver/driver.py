# 2021 Adelta
# https://github.com/A-delta


from sys import platform
from os import system, path, chdir, getcwd, getenv, kill
from requests import request
from random import randint
from json import dumps, load
import urllib3, threading, socket, requests
import time
import subprocess, psutil

urllib3.disable_warnings()


class Driver:
    def __init__(self, verbose):
        """
        Creates a Driver object.

        :param verbose: for development purposes only.
        """

        self.platform = platform
        self.driver_path = path.join(getcwd(), "driver")
        self.verbose = verbose

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
            config_file_path = f"{getenv('HOME')}/.config/RaspiMote/pi_ip.raspimote"
        elif self.platform == "win32":
            config_file_path = f"{getenv('APPDATA')}\\RaspiMote\\pi_ip.raspimote"
        
        if path.isfile(config_file_path):
            pi_ip = open(config_file_path, 'r')
            self.ip = load(pi_ip)["ip"]
            pi_ip.close()
        else:
            self.ip = input("Raspberry Pi's IP address : ")


        with open(config_file_path, 'w') as pi_ip:
            pi_ip.write(dumps({"ip": self.ip, "code": self.code}))


    def new_ip(self):
        if self.platform == "linux":
            config_file_path = f"{getenv('HOME')}/.config/RaspiMote/pi_ip.raspimote"
        elif self.platform == "win32":
            config_file_path = f"{getenv('APPDATA')}\\RaspiMote\\pi_ip.raspimote"
        
        self.ip = input("Raspberry Pi's IP address : ")


        with open(config_file_path, 'w') as pi_ip:
            pi_ip.write(dumps({"ip": self.ip, "code": self.code}))
        
        return_to_est = self.establish_connection()
        
        return return_to_est


    def establish_connection(self):
        """
        This method establish connection with the Raspberry Pi by sending it a request.


        :return:
        """

        url = f"https://{self.ip}:{self.port}/connect"
        content = {"code": self.code}
        headers = {"Content-Type": "application/json"}
        content = dumps(content)
        try:
            connection = request('CONNECT', url, data=content, headers=headers, verify=False)
            return connection.text == "True"
        except requests.exceptions.ConnectionError:
            new_ip = input(f"The driver is unable to connect to your Pi.\nDo you want to modidy the Pi's IP adress?\nCurrently, the IP adress is \"{self.ip}\".\n\n(Y/n)  ")
            new_ip = new_ip.lower()
            if new_ip == "y" or new_ip == "" or new_ip == "yes":
                return_to_main = self.new_ip()
                return return_to_main
            else:
                print("Aborting process.")
                exit()
        

    def watchdog(self):
        time.sleep(2)
        address = "https://localhost:"+str(self.port)
        while True:
            try:
                r = requests.post(address)
                time.sleep(3)
            except:
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

        if self.verbose:
            log_level = ''
        else:
            log_level = "--log-level critical"

        if self.platform == "win32":
            print("Only HTTP for the moment.")
            system('python wsgi_waitress.py')

        elif self.platform == "darwin":
            print("System not supported for the moment.")

        elif self.platform == "linux":
            system(f"gunicorn3 {log_level} --certfile cert.pem --keyfile key.key --bind 0.0.0.0:9876 wsgi_gunicorn:app")  # Run the HTTPS server.

        else:
            print("System not supported.")

        watchdog.start()
