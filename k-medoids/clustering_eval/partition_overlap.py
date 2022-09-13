# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:06:52 2021

@author: gulrch
"""

import numpy as np


def jaccard_seq(x, y):
    len_x = len(x)
    len_y = len(y)
    fst, snd = (x, y) if len_x < len_y else (y, x)
    num_intersect = len(set(fst).intersection(snd))
    
    #Jaccard score    
    return (num_intersect / (len_x + len_y - num_intersect))

def compute_jaccard_similarity_score(x, y):
    """
    Jaccard Similarity J (A,B) = | Intersection (A,B) | /
                                    | Union (A,B) |
    """
    intersection_cardinality = len(set(x).intersection(set(y)))
    union_cardinality = len(set(x).union(set(y)))
    return intersection_cardinality / float(union_cardinality)

def compare(labels1, labels2, NUMBER_OF_CLUSTERS):
    results = np.zeros((NUMBER_OF_CLUSTERS,NUMBER_OF_CLUSTERS))
    for n1 in range(0, NUMBER_OF_CLUSTERS):
        indexes1 = np.where(labels1 == n1)
        for n2 in range(0, NUMBER_OF_CLUSTERS):
            indexes2 = np.where(labels2 == n2)
            score = jaccard_seq(indexes1[0], indexes2[0])
            results[n1][n2] = int(score*100)
            #print ("Cluster "+str(n1)+" and cluster "+str(n2)+ ": "+ str(score))
    return results