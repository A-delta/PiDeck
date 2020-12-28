from change_volume import change_volume_lnx
from keyboard_actions import type_text
from json import loads

"""config = [
    {"pin": 21, "function": "example_function"},
    {"pin": 20, "function": "example_function2"}
]"""


def process(json):
    #print("Processing...")

    print(json)


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

    if type_device == "ADC" and pin == 0:
        sound_conf = loads(open("/home/louis/.config/RaspiMote/sound_conf.raspimote").read())
        change_volume_lnx(value, sound_conf)

    elif type_device == "button":
        if pin == 26:
            type_text("linux", 'α')
        elif pin == 19:
            pass
        elif pin == 13:
            pass
        elif pin == 6:
            pass



"""def example_function(json):
    print("I'm an example.")

def example_function2(json):
    print("I'm another example.")

def find_associate_function(json):
    print("I'm useless for now")"""