# -*- coding: utf-8 -*-

from subprocess import run as cmdrun, PIPE as cmdPIPE
from math_functions import take_closest

def change_volume_lnx(level, sound_conf):
    vol = cmdrun(["amixer", "get" ,"Master"], stdout=cmdPIPE)
    vol = str(vol.stdout).split("[")[1].replace("]", "").replace("%", "")
    take_closest(sound_conf, vol)