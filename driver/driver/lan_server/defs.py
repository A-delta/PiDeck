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
    # old  {'type': 'usb_hid', 'name': 'keyboard_0', 'device_key': 'key_8', 'action_type': 'press_key', 'key': 'v'}
    #  new {'type': 'usb_hid', 'name': 'keyboard_0', 'function': {'key': {'action_type': 'press_key', 'to_press': 'key_t'}}}
    #  {'type': 'usb_hid', 'name': 'mouse_0', 'device_key': 'button_left', 'action_type': 'run_command', 'command': 'tyet'}
    #  {'type': 'button', 'gpio': 2, 'action_type': 'type_text', 'text': 'test'}
    #  {'type': 'adc', 'channel': 1, 'action_type': 'change_volume'}
    # {'type': 'xbox_one_gamepad', 'button': 'btn_mode', 'action_type': 'run_command', 'command': 'a'}


    device_type = data["type"]

    if device_type == "usb_hid":
        name == data["name"]
        function = data["function"]

        


    elif device_type == "xbox_one_gamepad":
        pass

    elif device_type == "adc":
        pass

    elif device_type == "button":
        pass







def remove_action(path):
    pass

def get_actions(path):
    pass
