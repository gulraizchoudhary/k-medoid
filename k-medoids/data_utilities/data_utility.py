"""
This module reads and manipulates the raw data

APIs 
* read_file : read from file and create numpy array of list
    * parameters
        - file_path : (string) file path to supply to data_utilities

* get_features : flatten strings from numpy array of list and unique them
    * parameters
        - np_data : numpy array of list
"""

import numpy as np
from itertools import chain
import os
import json
import random, math



#Select random samples from a dictionary
def sample_from_dict(d, RANDOM_SAMPLES):
    keys = random.sample(list(d), RANDOM_SAMPLES)
    values = [d[k] for k in keys]
    return dict(zip(keys, values))

def covert2NumpyArray(plist):
    data_list = []
    for p in plist:
        data_list.append(np.array(plist[p]))
    return np.array(data_list)

def read_file(file_path):
    data_list = []

    with open(file_path, 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            line = line.split(' ')
            data_list.append(np.array(line))

    return np.array(data_list)

def read_file_labels(file_path):
    data_list = []

    with open(file_path, 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            line = line.split(' ')
            data_list.append(int(line[0]))

    return np.array(data_list)

def read_and_filter(file_path, min_feature, size):
    data_list = []

    with open(file_path, 'r', encoding = "ISO-8859-1") as f:
        for line in f.readlines():
            if len(data_list) == size:
                break
                
            line = line.rstrip()
            line = line.split(' ')

            if len(line) >= min_feature and line != ['']:
                data_list.append(np.array(line))

    return np.array(data_list)

def get_features(np_data):
    np_data_1d = list(chain.from_iterable(np_data))
    unique_set = set(np_data_1d)
    unique_set.discard('')
    features = np.array(list(unique_set))
    return features

def write_file(data_seq, file_path, mode = 'w'):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, mode) as f:
        j = 0
        for i in data_seq:
            s = ' '.join([j for j in i])
            f.write(s)    
            f.write('\n')
            j = j + 1
            
def write_labels(data_seq, file_path, mode = 'w'):
    with open(file_path, mode) as f:
        j = 0
        for i in data_seq:
            f.write(str(i))    
            f.write('\n')
            j = j + 1
            
def write_Medoids(data_seq, data, labels, file_path, mode = 'w'):
    #count the number of clusters and disease sets in the clusters
    unique, counts = np.unique(labels, return_counts=True)
    
    with open(file_path, mode) as f:
        j = 0
        for i in data_seq:
            f.write(str(i)+" "+str(data[i])+" "+str(counts[j]))    
            f.write('\n')
            j = j + 1
def write_occurrences(occ, file_path, mode = 'w'):
    with open(file_path, mode) as f:
        j = 0
        for i in occ:
            f.write(str(i)+" "+str(occ[i]))    
            f.write('\n')
            j = j + 1


#Write data in a file generated after getting frequent itemsets 
def write_itemsets(data_seq, file_path, isPatient, mode = 'w'):
    with open(file_path, mode) as f:
        j = 0
        for key in data_seq:
            for line in data_seq[key]:
                val = line.pop()
                if isPatient:
                    line = listToString(line) +" "+str(val)
                else:
                    line = listToString(line)
                f.write(str(line))    
                f.write('\n')
                j = j + 1


# Function to convert   
def listToString(s):  
    # initialize an empty string 
    str1 = " " 
    # return string   
    return (str1.join(s))