config = [
    {"pin": 21, "function": "example_function"},
    {"pin": 20, "function": "example_function2"}
]


def process(json):
    print("Processing...")

    if "inventory" in json.keys():
        makeInventory(json)
    else:
        find_associate_function(json)

def makeInventory(json):
    print("Got inventory :", json)


def example_function(json):
    print("I'm an example.")

def example_function2(json):
    print("I'm another example.")

def find_associate_function(json):
    print("I'm useless for now")