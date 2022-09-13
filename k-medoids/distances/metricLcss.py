# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:47:30 2019

@author: gulrch
"""
#This implementation is based on strsim library in python
#-The library also contains the many other similarity measures such as edit distance etc. 
#https://pypi.org/project/strsim/#optimal-string-alignment


from distances import lcss

def metricLcss(x, y):
    
    len_x = len(x)
    len_y = len(y)
    
    #Metriclcs distance score    
    return 1-lcss.lcss(x,y)/max(len_x, len_y)