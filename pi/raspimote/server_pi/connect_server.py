# 2021 RaspiMote
# https://github.com/RaspiMote


"""
Build a web server to establish connection between the driver and the Pi.
"""
from flask import Flask, request
from os import getenv, path, mkdir, system
from json import dumps as jdp
from threading import Thread
from time import sleep

app = Flask(__name__)

def killme():
    sleep(2)
    system("sh ./stop_server.sh > /dev/null")

@app.route('/connect', methods = ['POST'])
def connect():
    k = Thread(name='Kill server', target=killme)

    ip = request.remote_addr
    home = getenv('HOME')


    config_folder = path.join(home, ".config","RaspiMote")

    if not path.isdir(config_folder):
        mkdir(config_folder)

    connection_file = open(path.join(config_folder, "connection.raspimote"), "w+", encoding="utf-8")

    data = jdp({"ip": ip, "code": request.json["code"], "platform": request.json["platform"]})
    connection_file.write(data)
    connection_file.close()
    k.start()
    return "True"

@app.route('/')
def test():
    return 'UP !'