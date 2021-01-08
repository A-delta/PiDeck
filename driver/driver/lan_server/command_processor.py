# 2021 Adelta
# https://github.com/A-delta

from built_in_fcn.actions import type_text, run_command


def process(json):
    print("Processing", json)

    if "inventory" in json.keys():
        makeInventory(json)
    else:
        parse_data(json)


def makeInventory(json):
    print("Got inventory :", json)


def parse_data(json):
    request = json["request"]
    type_device = request["type"]
    pin = int(request["pin"])
    value = request["value"]
    try:
        extra = request["extra"]
    except:
        extra = None

    key_to_char = {
        "KEY_Q": "α",
        "KEY_W": "β",
        "KEY_E": "π",
        "KEY_R": "ω",
        "KEY_T": "Δ",
        "KEY_Y": "≈",
        "KEY_U": "√",
        "KEY_I": "∞",
        "KEY_O": "≠",
    }

    key_to_browser = {
        "KEY_P": "https://pronote.larmand.fr/pronote/eleve.html",
        "KEY_SEMICOLON": "https://mail.google.com/mail/u/1/#inbox",
        "KEY_L": "https://drive.google.com/drive/u/1/my-drive",
    }

    if type_device == "USB" and pin == 1 and int(extra) == 1:
        if value in key_to_char:
            type_text(key_to_char[value])
        elif value in key_to_browser:
            run_command(f"gio open {key_to_browser[value]}")
