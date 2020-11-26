def volume(old, new):
    old = int((old/255) * 100)
    new = int((old/255) * 100)
    if old < new:
        return(f"Volume UP, old={old}%, new={new}%")
    else:
        return(f"Volume DOWN, old={old}%, new={new}%")

def undefined():
    return("Pot #2")

def open_repo():
    return("open_repo button")

def enable_night_light():
    return("enable_night_light")

def disable_night_light():
    return("disable_night_light")