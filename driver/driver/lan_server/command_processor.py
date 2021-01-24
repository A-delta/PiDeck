# 2021 Adelta
# https://github.com/A-delta

from built_in_fcn.actions import type_text, run_command


def process(json):
    if "inventory" in json.keys():
        makeInventory(json)
    else:
        parse_data(json)


def makeInventory(json):
    print("Got Pi's inventory :", json)


def parse_data(json):
    """
    Here you will add your code to suit your needs.
    Do not delete the first chunk of code below.
    """
    request = json["request"]
    type_device = request["type"]
    pin = int(request["pin"])
    value = request["value"]
    try:
        extra = request["extra"]
    except:
        extra = None

    key_to_char = {  # Example of a USB keyboard that writes custom characters
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

    if type_device == "USB" and pin == 1 and int(extra) == 1:  # This is custom code that works for me.
        if value in key_to_char:
            type_text(key_to_char[value])
