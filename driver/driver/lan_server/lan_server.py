# 2021 Adelta
# https://github.com/A-delta

"""
Build a web server to receive RaspiMote's requests.
"""
from command_processor import process
import threading
from flask_cors import CORS
from flask import Flask, request
from json import load, loads
from os import path, getenv
from time import time

app = Flask(__name__)
CORS(app)

"""config_path = path.join(getenv("HOME"), ".config","RaspiMote")

file = load(open(path.join(config_path, "pi_ip.raspimote")))
pi_ip = file["ip"]
connection_code = file["code"]"""


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
            processor = threading.Thread(name='Processor', target=process, args=[json])
            processor.start()

            return "True"

@app.route('/config', methods = ['POST'])
def config():
    if request.remote_addr == "127.0.0.1":
        conf_req = loads(list(request.form.to_dict().keys())[0])
        with open ("trigger_actions.raspimote", "r") as trigger_actions:        
            trigger_actions = loads(trigger_actions.read())
        
    else:
        return '<h1>Not authorized.</h1><h2>Only localhost can configure RaspiMote.</h2>', 403