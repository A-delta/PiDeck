# -*- coding: utf-8 -*-

from os import system
from sys import platform
from keyboard import send as press, write


def press_key(action, value):
    """
    Do the specified action or simulate keystroke.
    action : "alphabet" or "numeral" for keypress simulation or "media" for other (see list)

    :param action: alphabet, numeral or media
    :param value: see allowed value in documentation
    :return:
    """
    if action == "alphabet" or action == 'numeral':
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
            system(f'xdotool key {value.upper()}')

        if platform == 'win32':
            press(f'{value}')

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
    """
    Write the specified text in the current window.

    :param text: A string
    :return:
    """
    if platform == 'linux':
        system(f'xdotool type "{text}"')

    if platform == 'win32':
        write(text)


def send_notification(title, text):
    """
    Display a notification with the specified title and text.

    :param title: Notification's title
    :param text: Notification's text
    :return:
    """

    if platform == 'linux':
        system(f"notify-send -a {title} -i RaspiMote -t 5000 '{text}'")

    elif platform == 'win32':
        system(f"powershell -Command \"&'.\\toast.ps1' '{title}' '{text}'")


def battery_level(level):
    """
    Display Raspberry Pi current battery level.
    :param level:
    :return:
    """

    send_notification("Raspimote", f"There remains {int(level)} % of power in the battery")


def change_volume(level):
    if platform == 'linux':
        system(f"amixer set Master {level}%")

    elif platform == 'win32':
        level = round(int(level) * 65535 / 100)
        system(f"nircmd.exe setsysvolume {level}")

def run_command(command):
    system(command)