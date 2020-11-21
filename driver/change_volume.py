# -*- coding: utf-8 -*-

from subprocess import run as cmdrun, PIPE as cmdPIPE
from math_functions import take_closest
from os import system as systex

def change_volume_lnx(level, sound_conf):
    current_vol = cmdrun(["amixer", "get" ,"Master"], stdout=cmdPIPE)
    current_vol = int(str(current_vol.stdout).split("[")[1].replace("]", "").replace("%", ""))
    current_vol = take_closest(sound_conf, current_vol)
    wanted_vol = take_closest(sound_conf, int(level))
    c = 1
    d = 1
    k = 0
    for step in sound_conf:
        k = k + 1
        if c == 1:
            if step == wanted_vol:
                wanted_step = k
                c = 0
        if d == 1:
            if step == current_vol:
                actual_step = k
                d = 0
    step_diff = wanted_step - actual_step
    if step_diff > 0:
        k = 0
        while k < step_diff:
            systex("xdotool key XF86AudioRaiseVolume")
            k = k + 1
    elif step_diff < 0:
        k = 0
        while k < abs(step_diff):
            systex("xdotool key XF86AudioLowerVolume")
            k = k + 1