# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:28:08 2019

@author: gulrch
"""

"""
This module calculate simple matching distance

parameters:
x : (numpy array) first string sequence
y : (numpy array) second string sequence

return:
(float) : Simple matching distance (1 - smd)
"""

def smd_seq(x, y):
    len_x = len(x)
    len_y = len(y)
    fst, snd = (x, y) if len_x < len_y else (y, x)
    num_intersect = len(set(fst).intersection(snd))
    
    #simple matching distance (1-smd)
    return 1-num_intersect/(len_x+len_y)