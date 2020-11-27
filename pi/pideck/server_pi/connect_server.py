# -*- coding: utf-8 -*-

"""
Build a web server to establish connection between the driver and the Pi.
"""

from flask import Flask, request
from os import getenv, path, mkdir, chdir, kill, getpid
from json import loads as jld, dumps as jdp
from signal import SIGINT
import threading
from time import sleep

pid = 0
app = Flask(__name__)

def run_server(pid_):
    app.run()
    global pid
    pid = pid_

def killme():
    sleep(2)
    global pid
    kill(pid, SIGINT)

@app.route('/connect', methods = ['CONNECT'])
def connect():
    k = threading.Thread(name='Kill server', target=killme)

    ip = request.remote_addr
    home = getenv('HOME')

    config_folder = path.join(home, "PiDeck")
    if not path.isdir(config_folder):
        mkdir(config_folder)

    connection_file = open(path.join(config_folder, "connection.pideck"), "w+", encoding="utf-8")

    connection_file.write(jdp({"ip": ip, "code": request.json["code"]}))
    print(jdp({"ip": ip, "code": request.json["code"]}))

    connection_file.close()
    k.start()
    return "True" # Return a value so the driver knows that the request was received without problems.