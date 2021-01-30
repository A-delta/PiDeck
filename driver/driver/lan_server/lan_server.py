# 2021 Adelta
# https://github.com/A-delta

"""
Build a web server to receive RaspiMote's requests.
"""
from command_processor import process
import threading
from flask_cors import CORS
from flask import Flask, request
from json import load, loads, dumps
from os import path, getenv
from time import time
from sys import platform

app = Flask(__name__)
CORS(app)

if platform == "linux":
    config_file_path = f"{getenv('HOME')}/.config/RaspiMote"
elif platform == "win32":
    config_file_path = f"{getenv('APPDATA')}\\RaspiMote"

file = load(open(path.join(config_file_path, "pi_ip.raspimote")))
pi_ip = file["ip"]
connection_code = file["code"]


@app.route('/action', methods = ['POST'])
def action():
    ip = request.remote_addr

    if pi_ip != ip:
        return '<h1>Not authorized.</h1><h2>IPs do not match.</h2>', 403
    else:
        json = request.json
        code = json["code"]

        if code != connection_code:
            return '<h1>Not authorized.</h1><h2>Codes do not match.</h2>', 403
        else:
            if json["request"] == "ping":
                print("It's a ping!")
                return "True"

            processor = threading.Thread(name='Processor', target=process, args=[json])
            processor.start()

            return "True"

@app.route('/config', methods = ['POST'])
def config():
    if request.remote_addr == "127.0.0.1":
        conf_req = loads(list(request.form.to_dict().keys())[0])
        try:
            with open(path.join(config_file_path, "trigger_actions.raspimote"), "r") as trg_actions:        
                trigger_actions = loads(trg_actions.read())
        except FileNotFoundError:
            trigger_actions = []
        new_trigger_actions = trigger_actions

        for action in trigger_actions:
            if action["port"] == conf_req["port"]:
                new_trigger_actions.remove(action)
        
        new_trigger_actions.append(conf_req)


        with open(path.join(config_file_path, "trigger_actions.raspimote"), "w") as trg_actions:
            trg_actions.write(dumps(new_trigger_actions))


        return "Configuration modified successfully."
        
        
    else:
        return '<h1>Not authorized.</h1><h2>Only localhost can configure RaspiMote.</h2>', 403

@app.route('/test')
def test():
    return 'UP !'