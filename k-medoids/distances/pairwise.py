"""
This module calculate pairwise distance for data that is a numpy array of list of string

parameters:
* X : (numpy array(list(string))) a numpy array of list of string
"""

import numpy as np
from itertools import combinations
from distances import jaccard
from distances import overlap
from distances import dice
from distances import bram
from distances import smc
from distances import lcss
from distances import metricLcss
from distances import overlapLcss
from distances import me
from distances import s3m
from distances import tss

def calculate_pairwise_distance(X, sm):
    # TODO : this function is very slow need improvement
    data_size = X.shape[0]
    precomputed = np.zeros((data_size, data_size))
    iterator = combinations(range(X.shape[0]), 2)
    
    
    #overlapMetri, Overlap = sequence set similarity
    if(sm =='sss'):
        for i, j in iterator: 
            precomputed[i, j] = tss.tss(X[i], X[j],0.5,0.5) 
    
    #jdr, jaccard distance ratio
    if(sm =='jdr'):
        for i, j in iterator: 
            precomputed[i, j] = jaccard.jaccard_seq(X[i], X[j])  
    #overlap, overlap co-efficient
    if(sm =='overlap'):
        for i, j in iterator: 
            precomputed[i, j] = overlap.overlap_seq(X[i], X[j])  
            
     #dice, dice similarity index 
    if(sm =='dice'):
        for i, j in iterator: 
            precomputed[i, j] = dice.dice_seq(X[i], X[j])  
            
     #bram, bram similarity index 
    if(sm =='bram'):
        for i, j in iterator: 
            precomputed[i, j] = bram.bram_seq(X[i], X[j])  
    
      #SMD, simple matching distance 
    if(sm =='smd'):
        for i, j in iterator: 
            precomputed[i, j] = smc.smd_seq(X[i], X[j]) 
            
      #LCS,longest common subsequences  
    if(sm =='lcss'):
        for i, j in iterator: 
            precomputed[i, j] = lcss.lcss(X[i], X[j]) 
    
     #MetricLCS,longest common subsequences  
    if(sm =='mlcss'):
        for i, j in iterator: 
            precomputed[i, j] = metricLcss.metricLcss(X[i], X[j]) 
    
    #overlapLcss
    if(sm =='overlapLcss'):
        for i, j in iterator: 
            precomputed[i, j] = overlapLcss.overlapLcss(X[i], X[j]) 
                
     #Monge-Elkan
    if(sm =='me'):
        for i, j in iterator: 
            precomputed[i, j] = me.me(X[i], X[j]) 

    #S3M
    if(sm =='s3m'):
        for i, j in iterator: 
            precomputed[i, j] = s3m.s3m(X[i], X[j],0.5,0.5)

    # Make symmetric and return
    return precomputed + precomputed.T - np.diag(np.diag(precomputed))