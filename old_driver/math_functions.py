# -*- coding: utf-8 -*-

def take_closest(sound_conf, number): # Function which takes the closest value to a number in a list.
    from bisect import bisect_left
    
    pos = bisect_left(sound_conf, number)
    if pos == 0:
        return sound_conf[0]
    if pos == len(sound_conf):
        return sound_conf[-1]
    before = sound_conf[pos - 1]
    after = sound_conf[pos]
    if after - number < number - before:
       return after
    else:
       return before