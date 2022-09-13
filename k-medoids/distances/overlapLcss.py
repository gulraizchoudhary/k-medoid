# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 13:33:47 2019

@author: gulrch
"""

from distances import lcss

def overlapLcss(x, y):
    
    len_x = len(x)
    len_y = len(y)
    
    #Metriclcs distance score    
    return 1-lcss.lcss(x,y)/min(len_x, len_y)