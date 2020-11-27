# -*- coding: utf-8 -*-

"""
Build a web server to establish connection between the driver and the Pi.
"""

from flask import Flask, request
from os import getenv, path, mkdir, chdir, isdir
from json import loads as jld, dumps as jdp

app = Flask(__name__)

@app.route('/connect', methods = ['CONNECT'])
def connect():
    ip = request.remote_addr
    home = getenv('HOME')

    config_folder = path.join(home, "PiDeck")
    if not path.isdir(config_folder):
        mkdir(config_folder)

    connection_file = open(path.join(config_folder, "connection.pideck"), "w+", encoding="utf-8")

    connection_file.write(jdp({"ip": ip, "code": request.json["code"]}))
    print(jdp({"ip": ip, "code": request.json["code"]}))

    connection_file.close()

    return "True" # Return a value so the driver knows that the request was received without problems.