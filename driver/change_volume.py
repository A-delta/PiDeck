# -*- coding: utf-8 -*-

def change_volume_lnx(level, sound_conf):
    from subprocess import run as cmdrun, PIPE as cmdPIPE
    from math_functions import take_closest
    from os import system as systex

    current_vol = cmdrun(["amixer", "get" ,"Master"], stdout=cmdPIPE) # Run the command "amixer get Master", and get its return, which contains the current volume level.
    current_vol = int(str(current_vol.stdout).split("[")[1].replace("]", "").replace("%", "")) # In the return of the function, isolate the current volume level (in %) as an integer.
    current_vol = take_closest(sound_conf, current_vol) # Take the closest value to the current volume level in the sound_conf.
    wanted_vol = take_closest(sound_conf, int(level)) # Take the closest value to the wanted volume in the sound_conf.
    c = 1
    d = 1
    k = 0
    for step in sound_conf:
        k = k + 1
        if c == 1:
            if step == wanted_vol:
                wanted_step = k # Find the step which corresponds to the wanted volume.
                c = 0
        if d == 1:
            if step == current_vol:
                actual_step = k # Find the step which corresponds to the current volume.
                d = 0
    step_diff = wanted_step - actual_step
    if step_diff > 0:
        k = 0
        while k < step_diff:
            systex("xdotool key XF86AudioRaiseVolume") # If the difference between the wanted step and the actual step is positive, increase the volume through the media keys.
            k = k + 1
    elif step_diff < 0:
        k = 0
        while k < abs(step_diff):
            systex("xdotool key XF86AudioLowerVolume") # If the difference between the wanted step and the actual step is negative, decrease the volume through the media keys.
            k = k + 1

def change_volume_mac(level):
    from os import system as systex

    systex(f"volume {level}") # Simply change volume (uses module mac-volume).

def change_volume_win(level):
    from os import system as systex

    level = round(int(level) * 65535 / 100)
    systex(f"nircmd.exe setsysvolume {level}")