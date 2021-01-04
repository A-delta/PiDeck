# 2020 Adelta
# https://github.com/A-delta


from sys import platform
from os import system, path, chdir, getcwd, getenv
from requests import request
from random import randint
from json import dumps


class Driver:
    def __init__(self):

        self.platform = platform
        self.driver_path = path.join(getcwd(), "driver")

        self.code = str(randint(0, 9999999))
        self.ip = ''
        self.port = 9876

        self.load_config()

    def load_config(self):
        """Will check for saved config.
        If none, -> self.configure()"""
        # debug :
        self.ip = "192.168.1.37"

        if self.platform == "linux":
            config_folder = "HOME"
        elif self.platform == "win32":
            config_folder = "APPDATA"

        config_path = path.join(getenv(config_folder), ".config", "RaspiMote")

        with open(path.join(config_path, "pi_ip.raspimote"), 'w') as pi_ip:
            pi_ip.write(dumps({"ip": self.ip, "code": self.code}))


        # TRADUIRE CA
        """    home = getenv('HOME')
    if platform == 'linux':
        home = getenv('HOME')
        home_no_slash = f'{home}/.config/RaspiMote'
        home = f'{home_no_slash}/'
    if platform == 'windows':
        home = getenv('APPDATA')
        home_no_slash = f'{home}\\RaspiMote'
        home = f'{home_no_slash}\\'
    systex(f'mkdir -p "{home_no_slash}"')
    with open (f"{home}pi_ip.raspimote", 'w') as pi_ip:
        pi_ip.write(dumps({"ip": ip, "code": str(random)}))"""

    def configure(self):
        """Ask for IP and stuff and save it"""
        pass

    def establish_connection(self):

        url = f"https://{self.ip}:{self.port}/connect"
        content = {"code": self.code}
        headers = {"Content-Type": "application/json"}
        content = dumps(content)
        x = request('CONNECT', url, data=content, headers=headers, verify=False)
        return x.text == "True"

    def run(self):
        chdir(path.join(self.driver_path, "lan_server"))

        if self.platform == "win32":
            print("Only HTTP for the moment.")
            #system('python wsgi_waitress.py')

        elif self.platform == "darwin":
            print("System not supported for the moment.")

        elif self.platform == "linux":
            system("gunicorn --certfile cert.pem --keyfile key.pem --bind 0.0.0.0:9876 wsgi_gunicorn:app")  # Run the HTTPS server.

        else:
            print("System not supported.")