# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 18:57:14 2020

@author: gulrch
"""
import networkx as nx

#Construct occurrence graph from a list and return frequencies of every node
def getFrequencies(data):
    
    
    #construct a digraph
    G = nx.DiGraph()
    
    dlist = dict()
    

    for index in range(0,len(data)):
        diseases= data[index]
        flag = True
        prev = ""
        G.add_node("STR")
        for disease in diseases:
            G.add_node(disease)
            
            if flag:
                flag = False
                prev ="STR"
                        
            if not G.has_edge(prev, disease):  
                G.add_edge(prev, disease)
                G.edges[prev, disease]["patient"] = []

            if G.edges[prev, disease]:
                G.edges[prev, disease]["patient"].append(index)
            else:
                G.edges[prev, disease]["patient"]=[index]
                
            prev = disease
            
            if disease in dlist:
                dlist[disease].append(index)
            else:
                 dlist[disease] = [index] 
    
    attr = dict()
    for edg in G.edges:
        attr[edg] = G.edges[edg[0],edg[1]]
    
    #Add all patients to start node             
    dlist["STR"] = list(range(0, len(data)))
    
    #set nodes attribute to patient list where they occurred 
    for node in G:
        G.nodes[node]['patient'] = dlist[node]
    nx.set_edge_attributes(G, attr)
    
    return get_freq_occurrence(G)


#count the occurrence of diseases from a graph
def get_freq_occurrence(G):
    occ = dict()
    for node in G:
        if node !="STR":
            occ[node] = len(G.nodes[node]['patient'])
            
    return dict(sorted(occ.items(), key=lambda x: x[1], reverse=True))