# -*- coding: utf-8 -*-

"""
Build a web server to receive RaspiMote's requests.
"""

from flask import Flask, request
from os import getenv, path
from json import load

app = Flask(__name__)

config_path = path.join(getenv("HOME"), ".config","RaspiMote")

file = load(open(path.join(config_path, "pi_ip.raspimote")))
pi_ip = file["ip"]
connection_code = file["code"]


@app.route('/action', methods = ['POST'])
def action():

    ip = request.remote_addr

    if pi_ip != ip:
        return '<h1>Not authorized.</h1><h2>IPs do not match.</h2>', 401  # Not authorized if the IPs don't match.
    else:
        json = request.json  # Retreive json data from the request.
        code = json["code"]
        data_type = json["request"]["type"]
        pin = json["request"]["pin"]
        value = json["request"]["value"]

        print(json)

        if code != connection_code:
            return '<h1>Not authorized.</h1><h2>Codes do not match.</h2>', 401  # Not authorized if the connection codes don't match.
        else:
            return "True"  # Return a value so the Pi knows that the request was received without problems.