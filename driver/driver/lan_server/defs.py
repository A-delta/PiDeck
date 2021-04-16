from json import loads
import json


def get_conf_file(path):
    try:
        with open(path, "r") as trg_actions:
            #print("Reading trigger_actions file")
            trigger_actions = loads(trg_actions.read())
            return trigger_actions
    except Exception:
        print("An error occured")
        trigger_actions_file = open(path, "w", encoding="utf-8")
        print("Created new trigger_actions file")
        trigger_actions = {}
        trigger_actions_file.write(json.dumps(trigger_actions))

        return trigger_actions    

def save_conf_file(path, new_conf):
    to_save = json.dumps(new_conf, indent=4)

    with open(path, "w") as old_conf:
            old_conf.write(to_save)
            return



def write_action(path, request):
    conf = get_conf_file(path)

    device_type = request["type"]
    name = request["name"]
    function = request["function"]

    when = function["when"]
    action_type = function["action_type"]
    data = function["data"]

    print(f"\nAdding : {device_type} called {name}")
    print(f"when [{when}] : {action_type} -> {data}")



    if device_type not in conf.keys():
        conf.update({device_type: []})

    i=0
    for e in conf[device_type]:
        if name in e.keys():
            conf[device_type][i].update(function)
            save_conf_file(path, conf)
            return
        i+=1

    conf[device_type].append({name: function})

    save_conf_file(path, conf)



def delete_action(path, request):
    pass



def get_actions_file(path):
    return get_conf_file(path)
