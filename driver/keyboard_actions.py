# -*- coding: utf-8 -*-

def press_key(platform, todo, value):
    if todo == "alphabet":
        if platform == 'linux':
            from os import system as systex

            systex(f"xdotool key {value}")

        elif platform == 'windows':
            from keyboard import send as press

            press(value)

        else:
            print("Not implemented.")

    elif todo == "media":
        if platform == 'linux':
            from os import system as systex

            if value == "volup":  
                systex('xdotool key XF86AudioRaiseVolume')
            elif value == "voldown":
                systex('dotool key XF86AudioLowerVolume')
            elif value ==  "mute":
                systex('xdotool key XF86AudioMute')
            elif value == "pp":
                systex('xdotool key XF86AudioPlay')
            elif value == "next":
                systex('xdotool key XF86AudioNext')
            elif value == "previous":
                systex('xdotool key XF86AudioPrev')

        elif platform == 'windows':
            from keyboard import send as press

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

    elif todo == "fn":
        if platform == 'linux':
            from os import system as systex
            
            systex(f'xdotool key F{value}')

        if platform == 'windows':
            from keyboard import send as press
            
            press(f'f{value}')

        else:
            print('Not implemented.')

    elif todo == "other":
        if platform == "linux":
            from os import system as systex

            if value == "psc":
                systex('xdotool key Print')
            elif value == "pos1":
                systex('xdotool key Home')
            elif value == "end":
                systex('xdotool key End')
            elif value == "del":
                systex('xdotool key Delete')
            elif value == "enter":
                systex('xdotool key Return')
            elif value == "backspace":
                systex('xdotool key BackSpace')
            elif value == "tab":
                systex('xdotool key Tab')
            elif value == "pup":
                systex('xdotool key Page_Up')
            elif value == "pdown":
                press('xdotool key Page_Down')
            elif value == "shift":
                systex('xdotool key Shift_L')
            elif value == "ctrl":
                systex('xdotool key Control_L')
            elif value == "alt":
                systex('xdotool key Alt_L')
            elif value == "super":
                systex('xdotool key Super_L')

        elif platform == 'windows':
            from keyboard import send as press

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