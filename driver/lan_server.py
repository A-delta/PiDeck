# -*- coding: utf-8 -*-

"""
Build a web server to receive RaspiMote's requests.
"""

from flask import Flask, request
from os import getenv
from json import loads as jld
from sys import platform as plt
import time
app = Flask(__name__)


@app.route('/action', methods = ['POST'])
def action():
    start = time.time()

    platform = plt
    if platform == 'linux':
        home = getenv('HOME')
        home = f'{home}/.config/PiDeck/'
    if platform == 'win32':
        home = getenv('APPDATA')
        home = f'{home}\\PiDeck\\'
    ip = request.remote_addr
    try:
        with open (f"{home}pi_ip.pideck", "r") as ip_json: # Check that the request is from the Pi and not from a malicious person who wants to control your computer.
            ip_file = ip_json.jld
            pi_ip = ip_file.read()["ip"]
            connection_code = ip_file.read()["code"]
    except:
        pi_ip = ip

    mid = time.time()

    print(mid-start, "before ip verification")

    if pi_ip != ip:
        return '<h1>Not authorized.</h1><h2>IPs do not match.</h2>', 401 # Not authorized if the IPs don't match.
    else:
        json = request.json # Retreive json data from the request.
        code = json["code"]
        data_type = json["request"]["type"]
        pin = json["request"]["pin"]
        value = json["request"]["value"]
        

        try:
            connection_code
        except NameError:
            connection_code = code
        if code != connection_code:
            return '<h1>Not authorized.</h1><h2>Codes do not match.</h2>', 401 # Not authorized if the connection codes don't match.
        else:
            return "True" # Return a value so the Pi knows that the request was received without problems.