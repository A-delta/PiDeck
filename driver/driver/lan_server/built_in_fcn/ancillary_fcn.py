# -*- coding: utf-8 -*-

def closest(array, number): # Function which takes the closest value to a number in a list.
    from bisect import bisect_left
    
    pos = bisect_left(array, number)
    if pos == 0:
        return array[0]
    if pos == len(array):
        return array[-1]
    before = array[pos - 1]
    after = array[pos]
    if after - number < number - before:
       return after
    else:
       return before