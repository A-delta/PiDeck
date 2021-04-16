from json import loads


def get_conf_file(path):
    try:
        with open(path, "r") as trg_actions:
            trigger_actions = loads(trg_actions.read())
    except FileNotFoundError:
        print("Created trigger_actions file")
        trigger_actions_file = file.open(path, "w", encoding="utf-8")
        trigger_actions = {}

    return trigger_actions


def add_action(path, request):
    data = get_conf_file(path)
    device_type = request["type"]
    name = request["name"]
    function = request["function"]

    if device_type == "usb_hid":
        print("USB")


    elif device_type == "xbox_one_gamepad":
        print("Gamepad")
        pass

    elif device_type == "adc":
        print("adc")
        pass

    elif device_type == "button":
        print("button")
        pass


def remove_action(path, request):
    pass



def get_actions(path):
    pass
