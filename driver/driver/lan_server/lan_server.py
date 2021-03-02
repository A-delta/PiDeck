# 2021 Adelta
# https://github.com/A-delta

"""
Build a web server to receive RaspiMote's requests.
"""
from command_processor import process
import threading
from flask_cors import CORS
from flask import Flask, request, send_file
from json import load, loads, dumps
from os import path, getenv
from time import time
from sys import platform


from built_in_fcn import actions

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
            if json["request"]["type"] != "ping":
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
        return '<h1>Not authorized.</h1><h2>Only <code>localhost</code> can configure RaspiMote.</h2>', 403

@app.route('/')
def config_ui():
    if request.remote_addr == "127.0.0.1":
        return send_file("ui/ui_model.html")
    else:
        return '<h1>Not authorized.</h1><h2>Only <code>localhost</code> can configure RaspiMote.</h2>', 403

@app.route('/style.css')
def config_css():
    if request.remote_addr == "127.0.0.1":
        return send_file("ui/style.css")
    else:
        return '<h1>Not authorized.</h1><h2>Only <code>localhost</code> can configure RaspiMote.</h2>', 403

@app.route('/initElements.js')
def config_js1():
    if request.remote_addr == "127.0.0.1":
        return send_file("ui/initElements.js")
    else:
        return '<h1>Not authorized.</h1><h2>Only <code>localhost</code> can configure RaspiMote.</h2>', 403

@app.route('/saveButton.js')
def config_js2():
    if request.remote_addr == "127.0.0.1":
        return send_file("ui/saveButton.js")
    else:
        return '<h1>Not authorized.</h1><h2>Only <code>localhost</code> can configure RaspiMote.</h2>', 403

@app.route('/showHide.js')
def config_js3():
    if request.remote_addr == "127.0.0.1":
        return send_file("ui/showHide.js")
    else:
        return '<h1>Not authorized.</h1><h2>Only <code>localhost</code> can configure RaspiMote.</h2>', 403

@app.route('/jquery-3.5.1.min.js')
def config_jquery():
    if request.remote_addr == "127.0.0.1":
        return send_file("ui/jquery-3.5.1.min.js")
    else:
        return '<h1>Not authorized.</h1><h2>Only <code>localhost</code> can configure RaspiMote.</h2>', 403

@app.route('/RaspiMote_logo.ico')
def config_rsp_ico():
    if request.remote_addr == "127.0.0.1":
        return send_file("../../../logo/RaspiMote_logo.ico")
    else:
        return '<h1>Not authorized.</h1><h2>Only <code>localhost</code> can configure RaspiMote.</h2>', 403

@app.route('/RaspiMote_logo_500px.png')
def config_rsp_png():
    if request.remote_addr == "127.0.0.1":
        return send_file("../../../logo/RaspiMote_logo_500px.png")
    else:
        return '<h1>Not authorized.</h1><h2>Only <code>localhost</code> can configure RaspiMote.</h2>', 403

@app.route('/loading.gif')
def gif_loading():
    if request.remote_addr == "127.0.0.1":
        return send_file("ui/loading.gif")
    else:
        return '<h1>Not authorized.</h1><h2>Only <code>localhost</code> can configure RaspiMote.</h2>', 403

@app.route('/get_inventory', methods = ['POST'])
def config_get_inventory():
    if request.remote_addr == "127.0.0.1":
        try:
            with open (path.join(config_file_path, "inventory.raspimote"), "r") as inventory:
                return inventory.read()
        except FileNotFoundError:
            return "INVENTORY_NOT_FOUND", 500
    else:
        return '<h1>Not authorized.</h1><h2>Only <code>localhost</code> can configure RaspiMote.</h2>', 403

@app.route('/test')
def test():
    return 'UP !'