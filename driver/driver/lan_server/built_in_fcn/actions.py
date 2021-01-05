# -*- coding: utf-8 -*-

from os import system
from sys import platform
from keyboard import send as press, write
from subprocess import run as sub_run, PIPE as sub_PIPE
from ancillary_fcn import closest


"""
`sound_conf` must be reimplemented!
"""


def press_key(action, value):
    if action == "alphabet":
        if platform == 'linux':
            system(f"xdotool key {value}")

        elif platform == 'win32':
            press(value)

        else:
            print("Not implemented.")

    elif action == "media":
        if platform == 'linux':

            if value == "volup":  
                system('xdotool key XF86AudioRaiseVolume')
            elif value == "voldown":
                system('dotool key XF86AudioLowerVolume')
            elif value ==  "mute":
                system('xdotool key XF86AudioMute')
            elif value == "pp":
                system('xdotool key XF86AudioPlay')
            elif value == "next":
                system('xdotool key XF86AudioNext')
            elif value == "previous":
                system('xdotool key XF86AudioPrev')

        elif platform == 'win32':

            if value == "volup":  
                press('volume up')
            elif value == "voldown":
                press('volume down')
            elif value ==  "mute":
                press('volume mute')
            elif value == "pp":
                press('play/pause media')
            elif value == "next":
                press('next track')
            elif value == "previous":
                press('previous track')

        else:
            print('Not implemented.')

    elif action == "fn":
        if platform == 'linux':           
            system(f'xdotool key F{value}')

        if platform == 'win32':
            press(f'f{value}')

        else:
            print('Not implemented.')

    elif action == "other":
        if platform == "linux":
            if value == "psc":
                system('xdotool key Print')
            elif value == "pos1":
                system('xdotool key Home')
            elif value == "end":
                system('xdotool key End')
            elif value == "del":
                system('xdotool key Delete')
            elif value == "enter":
                system('xdotool key Return')
            elif value == "backspace":
                system('xdotool key BackSpace')
            elif value == "tab":
                system('xdotool key Tab')
            elif value == "pup":
                system('xdotool key Page_Up')
            elif value == "pdown":
                press('xdotool key Page_Down')
            elif value == "shift":
                system('xdotool key Shift_L')
            elif value == "ctrl":
                system('xdotool key Control_L')
            elif value == "alt":
                system('xdotool key Alt_L')
            elif value == "super":
                system('xdotool key Super_L')

        elif platform == 'win32':
            if value == "psc":
                press('print screen')
            elif value == "pos1":
                press('home')
            elif value == "end":
                press('end')
            elif value == "del":
                press('delete')
            elif value == "enter":
                press('enter')
            elif value == "backspace":
                press('backspace')
            elif value == "tab":
                press('tab')
            elif value == "pup":
                press('page up')
            elif value == "pdown":
                press('page down')
            elif value == "shift":
                press('shift')
            elif value == "ctrl":
                press('ctrl')
            elif value == "alt":
                press('alt')
            elif value == "super":
                press('left windows')

        else:
            print('Not implemented.')

def type_text(text):
    if platform == 'linux':
        system(f'xdotool type "{text}"')

    if platform == 'win32':
        write(text)

def battery_level(level):
    if platform == 'linux':
        system(f"notify-send -a RaspiMote -i RaspiMote -t 5000 'There remains {level} % of power in the battery'")
    
    elif platform == 'win32':
        system(f"powershell -Command \"&'.\\toast.ps1' 'Raspimote' 'There remains {level} % of power in the battery.'")

def change_volume(level):
    if platform == 'linux':
        current_vol = sub_run(["amixer", "get" ,"Master"], stdout=sub_PIPE) # Run the command "amixer get Master", and get its return, which contains the current volume level.
        current_vol = int(str(current_vol.stdout).split("[")[1].replace("]", "").replace("%", "")) # In the return of the function, isolate the current volume level (in %) as an integer.
        current_vol = closest(sound_conf, current_vol) # Take the closest value to the current volume level in the sound_conf.
        wanted_vol = closest(sound_conf, int(level)) # Take the closest value to the wanted volume in the sound_conf.
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
                system("xdotool key XF86AudioRaiseVolume") # If the difference between the wanted step and the actual step is positive, increase the volume through the media keys.
                k = k + 1
        elif step_diff < 0:
            k = 0
            while k < abs(step_diff):
                system("xdotool key XF86AudioLowerVolume") # If the difference between the wanted step and the actual step is negative, decrease the volume through the media keys.
                k = k + 1

    elif platform == 'win32':
        level = round(int(level) * 65535 / 100)
        system(f"nircmd.exe setsysvolume {level}")