# 2020 Adelta
# https://github.com/A-delta

from built_in_fcn.actions import type_text
from built_in_fcn.actions import battery_level


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
    value = int(request["value"])

    if type_device == "button":
        if pin == 26:
            type_text('α')
        elif pin == 19:
            type_text('β')
        elif pin == 13:
            type_text('δ')
        elif pin == 6:
            battery_level(str(37))
