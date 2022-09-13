# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:26:44 2021

@author: gulrch
"""

from distances import lcss

#Temporal set similarity
def tss(x, y, p, q):
    
    len_x = len(x)
    len_y = len(y)
    fst, snd = (x, y) if len_x < len_y else (y, x)
    num_intersect = len(set(fst).intersection(snd))
    
    overlap = num_intersect/min(len_x, len_y)
    
    overlapLcss = lcss.lcss(x,y)/min(len_x, len_y)
    
    #Metriclcs distance score    
    return 1-((p*overlap) + (q*overlapLcss))