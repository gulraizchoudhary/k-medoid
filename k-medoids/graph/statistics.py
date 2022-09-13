# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:15:14 2019

@author: gulrch
"""
import matplotlib.pyplot as plt
import numpy as np

def get_firstOccrrences(G, SIZE):
    firstOccurr = dict()
    for disease in list(G.successors("STR")):
        firstOccurr[disease]=len(G.edges["STR", disease]["patient"])/SIZE
        
    return sorted(firstOccurr.items(), key=lambda x: x[1], reverse=True)

def plot_firstOccurrences(first, RESULT_PATH, TITLE):
    x, y = zip(*first)
    length = int(len(x)/10)
    xi = list(range(len(x)))
    plt.bar(x,y, align="center")
    plt.xticks(np.arange(min(xi), max(xi)+1, length))
    plt.title(TITLE)
    plt.xlabel('Diseases', fontsize=12)
    plt.ylabel('Probability', fontsize=12)
    plt.savefig(RESULT_PATH+'.png', dpi=600)    
    
def get_prob_occurrence(G, SIZE):
    occ = dict()
    for node in G:
        if node !="STR":
            occ[node] = len(G.nodes[node]['patient'])/SIZE
    return sorted(occ.items(), key=lambda x: x[1], reverse=True)

def get_freq_occurrence(G):
    occ = dict()
    for node in G:
        if node !="STR":
            occ[node] = len(G.nodes[node]['patient'])
    return sorted(occ.items(), key=lambda x: x[1], reverse=True)

#returns in degree, out degree and degree case of directed graph
def get_DG_degree(G):
    
    out_deg = [G.out_degree(n) for n in G.nodes()]
    in_deg = [G.in_degree(n) for n in G.nodes()]
    #The node degree is the number of edges adjacent to that node
    degree_of_nodes_adjacent = [G.degree(n) for n in G.nodes()] 
    avg_out= sum(out_deg[1:])/len(out_deg[1:])
    avg_in= sum(in_deg[1:])/len(in_deg[1:])
    avg_degree= sum(degree_of_nodes_adjacent[1:])/len(degree_of_nodes_adjacent[1:])
    
    return avg_out, avg_in, avg_degree, G.number_of_edges()

#returns degree of undirected graph
def get_degree(G):
    #The node degree is the number of edges adjacent to that node
    degree_of_nodes_adjacent = [G.degree(n) for n in G.nodes()] 
    avg_degree= sum(degree_of_nodes_adjacent)/len(degree_of_nodes_adjacent)
    
    return avg_degree, sum(degree_of_nodes_adjacent[1:]), G.number_of_edges()

def plot_out_Degree(G, RESULT_PATH, TITLE):
    degrees = [G.out_degree(n) for n in G.nodes()]
    degree_freq = np.array(degrees).astype('float')
    plt.figure(figsize=(12, 8))
    plt.stem(degree_freq)
    plt.ylabel("Frequence")
    plt.xlabel("Out degree")
    plt.title(TITLE)
    plt.savefig(RESULT_PATH+'.png', dpi=600)
    
def plot_in_Degree(G, RESULT_PATH, TITLE):
    degrees = [G.in_degree(n) for n in G.nodes()]
    degree_freq = np.array(degrees).astype('float')
    plt.figure(figsize=(12, 8))
    plt.stem(degree_freq)
    plt.ylabel("Frequence")
    plt.xlabel("In degree")
    plt.title(TITLE)
    plt.savefig(RESULT_PATH+'.png', dpi=600)