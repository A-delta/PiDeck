from json import loads


def get_conf_file(path):
    try:
        with open(path, "r") as trg_actions:
            trigger_actions_file = trg_actions
            trigger_actions = loads(trg_actions.read())
    except FileNotFoundError:
        print("Created trigger_actions file")
        trigger_actions_file = file.open(path, "w", encoding="utf-8")
        trigger_actions = {}

    return trigger_actions_file, trigger_actions


def add_action(path, request):
    file, actions = get_conf_file(path)
    """{'port': 'usb_keyboard_or_mouse', 'keyboard_key': 'scroll_up', 'action_type': 'run_command', 'command': 'echo test'}"""



def remove_action(path):
    pass

def get_actions(path):
    pass
