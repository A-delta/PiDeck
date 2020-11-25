# -*- coding: utf-8 -*-

"""
Build a web server to establish connection between the driver and the Pi.
"""

from flask import Flask, request
from os import getenv
from json import loads as jld, dumps as jdp

app = Flask(__name__)

@app.route('/connect', methods = ['CONNECT'])
def connect():
    ip = request.remote_addr
    home = getenv('HOME')
    home = f'{home}/.config/PiDeck/'
    with open (f"{home}connection.pideck", "w") as connection_file: # Save the data sent by the driver.
        connection_file.write(jdp({"ip": ip, "code": request.json["code"]}))
        print(jdp({"ip": ip, "code": request.json["code"]}))
    return "OK" # Return a value so the driver knows that the request was received without problems.