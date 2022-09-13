# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:20:38 2021

@author: gulrch
"""

from data_utilities import data_utility
from data_utilities import data_stat
from distances import pairwise
from clustering_eval import clustering_evaluation
from graph import dFrequencies as fr
import os
import time
from clustering_algorithms import kmedoids
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


LABLE = 'data_1200_800_16_5_1'

DATA_PATH = '../synthetic/'+LABLE+'.txt'

#third: number of clusters
NUMBER_OF_CLUSTERS = 10

#jdr, overlap, dice, bram, smd, mlcss, lcss, overlapLcss, s3m
SIMILARITY = "jdr"
LABELS_PATH = '../results/'+LABLE+'_'+SIMILARITY+'_labels_diff.txt'
KMEDOID_PATH = '../results/'+LABLE+'_'+SIMILARITY+'_kmedoid_diff.txt'
RESULT_PATH = '../results/'+LABLE+'_'+SIMILARITY+'_results_diff.txt'
FIGURE_PATH = '../results/'+LABLE+'_'+SIMILARITY
GRAPH_PATH = 'visuals/'

# read data
data = data_utility.read_file(DATA_PATH)

# pairwise distance
start = time.time()
pw_dist = pairwise.calculate_pairwise_distance(data, SIMILARITY)
pw_dist_time = time.time() - start

#Extract statistical information from dataset
print('=== Basic statistics === ')
print('Total number of sequences= '+str(len(data)))
print('Average length of sequences= '+str(data_stat.averageLength(data)))
diseases = data_stat.distinctDiagnosis(data)
print('Number of distinct diagnosis= '+str(len(diseases)))

#calculate overlap in dataset
overlap = data_stat.overlap(pw_dist)

set_count= data_stat.sequences_lenght(data)
data_stat.plot_bar_simple(overlap,FIGURE_PATH+'_set_overlap.png','Sets Overlap')
data_stat.plot_bar2(set_count,FIGURE_PATH+'_set_distribution.png','Set distribution')
data_stat.plot_bar(diseases,FIGURE_PATH+'_sequence_distribution.png','Sequence distribution')

# K-Medoids
print('=== Starting K-Medoids ===')
labels, kmedoids_row_index = kmedoids.cluster(data, NUMBER_OF_CLUSTERS, np.copy(pw_dist), np.array([]))
print('=== K-Medoids finished. === ')

data_utility.write_labels(labels, LABELS_PATH)
data_utility.write_Medoids(kmedoids_row_index,data, labels, KMEDOID_PATH)

print('=== Clustering Evaluation Start ===')
if os.path.exists(RESULT_PATH):
    os.remove(RESULT_PATH)
data_utility.write_file([['spd', 'spsd']], RESULT_PATH, 'a+')

spd = clustering_evaluation.spd_distance(data, labels, np.copy(pw_dist))
spsd = clustering_evaluation.spd_distance(data, labels, np.copy(pw_dist), 2)
data_utility.write_file([[str(spd), str(spsd)]], RESULT_PATH, 'a+')

print('=== Take a look at {} for the result ==='.format(RESULT_PATH))

clusters = []
 
for n in range(0, NUMBER_OF_CLUSTERS):
    indexes = np.where(labels == n)
    
    cluster = []

    for i in indexes:
        cluster =list(data[i])
        
    clusters.append(cluster)

#Construct graph of every indivisual cluster and display the frequent itemsets
for cl in range(0, NUMBER_OF_CLUSTERS):
    G = nx.DiGraph()
    medoid =data[kmedoids_row_index[cl]]
    for l in range(0,len(clusters[cl])):
        prevD = ""
        for d in clusters[cl][l]:
            G.add_node(d)
            if prevD!="":
                G.add_edge(prevD,d)
            prevD = d
            
    freq_all = fr.getFrequencies(clusters[cl])
   
    #color the representatives (medoids) and change the node size accordingly
    color_map = []

    nodes_size=[]
    
    frequencies ={}
    
    for node in G:
        frequencies[node]= (freq_all[node]/len(clusters[cl]))*100
        
        #set node size
        if(freq_all[node]>2):
            nodes_size.append(50*freq_all[node]/2)
        else:
            nodes_size.append(500)
    
        if node in medoid:
            color_map.append('yellow')
        else:
            color_map.append('cyan')
            
    nx.draw(G, node_color=color_map, node_size=nodes_size, with_labels = True)
    
    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
    
    #Plot histogram of frequent diseases in a cluster
    nfrequencies = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[0:10])
    xlabels = nfrequencies.keys()
    
    pos = np.arange(len(xlabels))
    width = 0.5     # gives histogram aspect to the bar diagram
    
    ax = plt.axes()
    ax.set_xticks(pos)
    ax.set_xticklabels(xlabels)
    ax.set_xlabel("ICD-10")
    ax.set_ylabel("Percent")
    ax.set_title('Cluster '+ str(cl))
    
    plt.bar(pos, nfrequencies.values(), width, color='b')
    ymin, ymax = plt.ylim()
    plt.ylim(ymin,100)
    plt.savefig(GRAPH_PATH+LABLE+'_'+SIMILARITY+"_in_cluster_"+str(cl)+"_histogram.png", bbox_inches = "tight") # save as png
    plt.show()