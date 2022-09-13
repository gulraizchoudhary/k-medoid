# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:38:43 2019

@author: gulrch
"""

import py_stringmatching as sm
import numpy as np

def TfIdf(x, y):
    len_x = len(x)
    len_y = len(y)
    
    x = np.array(x).tolist()
    y = np.array(y).tolist()
    
    mong = sm.MongeElkan()
    
    # (1-mong)
    return 1-mong.get_raw_score(list(x),list(y))/min(len_x,len_y)