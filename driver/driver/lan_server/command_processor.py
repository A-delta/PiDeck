# 2021 Adelta
# https://github.com/A-delta

from built_in_fcn.actions import type_text
from built_in_fcn.actions import battery_level
import subprocess


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

    if type_device == "USB" and pin == 4 and int(extra) == 1:
        if value in key_to_char:
            type_text(key_to_char[value])
