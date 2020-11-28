def process(json):
    print("Processing...")

    if "inventory" in json.keys():
        makeInventory(json)
    else:
        execute(json)

def makeInventory(json):
    print("Got inventory :", json)

def execute(json):
    print("Executing request :", json)

