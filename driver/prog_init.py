# -*- coding: utf-8 -*-

from os import getenv
from sys import platform

def check_platorm():
    if platform == 'linux':
        return 'linux'
    else:
        print('Sorry, your platform is not supported at the moment.') # Should be replaced by an alert messagebox in the future, with the possibility to submit an issue.
        return False

def init_lnx():
    home = getenv('HOME')
    try:
        with open (f'{home}/.config/PiDeck/sound_conf.pideck', 'r') as conf_file:
            sound_conf = conf_file.read()
    except:
        sound_conf = ""
        print('huh')
        # Run calibration process
    return {"sound_conf": sound_conf}