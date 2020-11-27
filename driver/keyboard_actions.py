def press_key(platform, todo, value):
    if todo == "alphabet":
        if platform == 'linux':
            from os import system as systex

            systex(f"xdotool key {value}")
        else:
            from keyboard import send as press

            press(value)
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
        else:
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
    elif todo == "fn":
        if platform == 'linux':
            from os import system as systex
            
            systex(f'xdotool key F{value}')
        else:
            from keyboard import send as press
            
            press(f'f{value}')
    elif todo == "other":
        if platform == "linux":
            print('Not implemented yet.')
        else:
            from keyboard import send as press

            if value == "psc":
                press('print screen')
            elif value == "pos1":
                press('home')
            elif value == "end":
                press('end')
            elif value == "ins":
                press('insert')
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