# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:32:21 2019

@author: gulrch
"""
#The Monge-Elkan similarity measure is a type of hybrid similarity measure that combines the benefits of sequence-based and set-based methods. 
#This can be effective for domains in which more control is needed over the similarity measure. 
#It implicitly uses a secondary similarity measure, such as Levenshtein to compute over all similarity score
import py_stringmatching as sm
import numpy as np

def me(x, y):
    len_x = len(x)
    len_y = len(y)
    
    x = np.array(x).tolist()
    y = np.array(y).tolist()
    
    mong = sm.MongeElkan()
    
    # (1-mong)
    return 1-mong.get_raw_score(list(x),list(y))/min(len_x,len_y)