"""
clustering evaluation measures library
"""
import numpy as np
import math

def spd_distance(data, labels, pair_wise_distances, degree = 1):  
    unique_labels = np.unique(labels)
    number_of_cluster = len(unique_labels)
    
    SPD_temp = 0
    
    for i in range(number_of_cluster):
        j = unique_labels[i]
        indices = np.where(labels == j)[0]
        cluster_size = len(indices)
        
        clusters_pair_distances = pair_wise_distances[np.ix_(indices, indices)]
        clusters_pair_distances = np.power(clusters_pair_distances, degree)
        SPD_temp = SPD_temp + (np.sum(np.sum(clusters_pair_distances,axis=1))) / cluster_size / 2
        
    return SPD_temp
