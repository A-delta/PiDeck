# -*- coding: utf-8 -*-

def check_platorm(): # Check if the current platform is one of the supported platforms.
    from sys import platform

    if platform == 'linux':
        return 'linux'
    else:
        print('Sorry, your platform is not supported at the moment.') # Should be replaced by an alert messagebox in the future, with the possibility to submit an issue.
        return False

def init_lnx():
    from os import getenv

    home = getenv('HOME')
    try:
        with open (f'{home}/.config/PiDeck/sound_conf.pideck', 'r') as conf_file: # Retreive the sound_conf for this computer.
            sound_conf = conf_file.read()
    except:
        sound_conf = ""
        print("sound_conf file doesn't exist.")
        # In that case, calibration process must be run.
    return {"sound_conf": sound_conf}

def calibrate_sound_lnx():
    from os import system as systex
    from subprocess import run as cmdrun, PIPE as cmdPIPE
    from math_functions import take_closest
    from time import sleep

    print("Please wait while we're calibrating volume change for your device.") # A dialog box telling the user not to touch anything must be shown.
    c = 1
    while c == 1: # Mute the sound (level 0).
        current_vol = cmdrun(["amixer", "get" ,"Master"], stdout=cmdPIPE) # Run the command "amixer get Master", and get its return, which contains the current volume level.
        current_vol = int(str(current_vol.stdout).split("[")[1].replace("]", "").replace("%", "")) # In the return of the function, isolate the current volume level (in %) as an integer.
        print(current_vol)
        if current_vol != 0: # Lower the volume until it's at 0 %.
            print(1)
            sleep(1)
            systex("xdotool key XF86AudioLowerVolume")
            sleep(1)
        else:
            print(2)
            sleep(1)
            systex("xdotool key XF86AudioLowerVolume")
            sleep(1)
            c = 0
    c = 1
    sound_conf = []
    last_vol = -10
    while c == 1:
        current_vol = cmdrun(["amixer", "get" ,"Master"], stdout=cmdPIPE) # Run the command "amixer get Master", and get its return, which contains the current volume level.
        current_vol = int(str(current_vol.stdout).split("[")[1].replace("]", "").replace("%", "")) # In the return of the function, isolate the current volume level (in %) as an integer.
        print(current_vol)
        if last_vol < current_vol: # Increase the volume step by step and save each value possible for the volume in a list.
            print(1)
            last_vol = current_vol
            sound_conf.append(current_vol)
            sleep(1)
            systex("xdotool key XF86AudioRaiseVolume")
            sleep(1)
        else:
            print(2)
            sleep(1)
            systex("xdotool key XF86AudioRaiseVolume")
            sleep(1)
            current_vol = cmdrun(["amixer", "get" ,"Master"], stdout=cmdPIPE) # Run the command "amixer get Master", and get its return, which contains the current volume level.
            current_vol = int(str(current_vol.stdout).split("[")[1].replace("]", "").replace("%", "")) # In the return of the function, isolate the current volume level (in %) as an integer.
            if last_vol == current_vol:
                c = 0
            else:
                sound_conf.append(last_vol)
    print(sound_conf) # Now, soundconf must be saved in "/home/username/.config/PiDeck/soundconf.pideck" and not only printed.