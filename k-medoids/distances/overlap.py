"""
This module calculate overlap's distance score

parameters:
x : (numpy array) first string sequence
y : (numpy array) second string sequence

return:
(float) : Overlap's distance socre (1 - Overlap's coefficient)
"""

def overlap_seq(x, y):
    len_x = len(x)
    len_y = len(y)
    fst, snd = (x, y) if len_x < len_y else (y, x)
    num_intersect = len(set(fst).intersection(snd))
    
    #Overlap coefficient score or overlap distance score (1-overlap coefficient)
    return 1-num_intersect/min(len_x, len_y)
