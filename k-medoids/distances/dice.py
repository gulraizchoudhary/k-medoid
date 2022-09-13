# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:41:53 2019

@author: gulrch
"""

"""
This module calculate overlap's distance score

parameters:
x : (numpy array) first string sequence
y : (numpy array) second string sequence

return:
(float) : dice distance socre (1 - dice similarity)
"""

def dice_seq(x, y):
    len_x = len(x)
    len_y = len(y)
    fst, snd = (x, y) if len_x < len_y else (y, x)
    num_intersect = len(set(fst).intersection(snd))
    
    #dice similarity distance score (1-dice)
    return 1-(2*num_intersect)/(len_x+len_y)