# 2020 Adelta
# https://github.com/A-delta

from user_functions.keyboard_actions import type_text


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
            type_text("linux", 'α')
        elif pin == 19:
            type_text("linux", 'β')
        elif pin == 13:
            type_text("linux", 'δ')
        elif pin == 6:
            type_text("linux", 'ε')
