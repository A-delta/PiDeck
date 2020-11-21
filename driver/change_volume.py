# -*- coding: utf-8 -*-

from subprocess import run as cmdrun, PIPE as cmdPIPE
from math_functions import take_closest

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
    step_diff = wanted_step - actual_step # It means that if `step_diff` is positive, volume must increase of `step_diff` and if `step_diff` is negative, volume must decrease of `abs(step_diff)`


change_volume_lnx(0, [0, 0, 15, 31, 43, 52, 60, 66, 71, 76, 79, 84, 87, 90, 93, 95, 99, 100])