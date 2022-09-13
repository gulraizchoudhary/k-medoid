# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:55:34 2019

@author: gulrch
"""

from distances import lcss

def s3m(x, y, p, q):
    len_x = len(x)
    len_y = len(y)
    fst, snd = (x, y) if len_x < len_y else (y, x)
    num_intersect = len(set(fst).intersection(snd))
    jac = (num_intersect / (len_x + len_y - num_intersect))
    
    lcs = lcss.lcss(x,y)/max(len_x, len_y)
    
    return (p*lcs)+(q*jac)
    