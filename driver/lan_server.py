# -*- coding: utf-8 -*-

"""
Build a web server to receive the PiDeck's requests.
"""

from flask import Flask, request
from waitress import serve
from sys import platform as plt
from os import getenv
from json import loads as jld

app = Flask(__name__)

@app.route('/action', methods = ['POST'])
def action():
    platform = plt
    if platform == 'linux':
        home = getenv('HOME')
        home = f'{home}/.config/PiDeck/'
    if platform == 'win32':
        home = getenv('APPDATA')
        home = f'{home}\\PiDeck\\'
    if platform == 'darwin':
        home = getenv('HOME')
        home = f'{home}/Library/Preferences/PiDeck/'
    ip = request.remote_addr
    try:
        with open (f"{home}pi_ip.pideck", "r") as ip_json: # Check that the request is from the Pi and not from a malicious person who wants to control your computer.
            ip_file = ip_json.jld
            print(ip_file)
            pi_ip = ip_file.read()["ip"]
            connection_code = ip_file.read()["code"]
    except:
        pi_ip = ip
    if pi_ip != ip:
        return '<h1>Not authorized.</h1><h2>IPs do not match.</h2>', 401 # Not authorized if the IPs don't match.
    else:
        json = request.json # Retreive json data from the request.
        code = json["code"]
        ID = json["id"]
        value = json["value"]
        # json["extra"] not implemented for the moment
        try:
            connection_code
        except NameError:
            connection_code = code
        if code != connection_code:
            return '<h1>Not authorized.</h1><h2>Codes do not match.</h2>', 401 # Not authorized if the IPs don't match.

        return "<h1>test</h1>" # This is a test.

serve(app, host='0.0.0.0', port=9876)