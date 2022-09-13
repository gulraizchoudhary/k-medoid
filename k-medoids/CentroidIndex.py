# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:24:04 2021

@author: gulrch
"""
#Evaluate the clusters
from data_utilities import data_utility
from clustering_eval import partition_overlap as comp
import numpy as np

NUMBER_OF_CLUSTERS = 16

LABLE = 'random_50000_filter_5_RUVWXYZ'
PATH = '../selectedResults/'
SIMILARITY = "overlapLcss"
LABELS_PATH1 = PATH+SIMILARITY+'/'+str(NUMBER_OF_CLUSTERS)+'/'+LABLE+'_'+SIMILARITY+'_labels_diff.txt'
SIMILARITY = "sss"
LABELS_PATH2 = PATH+SIMILARITY+'/'+str(NUMBER_OF_CLUSTERS)+'/'+LABLE+'_'+SIMILARITY+'_labels_diff.txt'


#uncomment these lines for synthetic data set
LABLE = 'data_1200_200_16_10_1'
SIMILARITY = "sss"
LABELS_PATH1 = PATH+'SyntheticResults/'+LABLE+'/'+LABLE+'_'+SIMILARITY+'_labels_diff.txt'
LABELS_PATH2 = PATH+'SyntheticResults/groundtruth/'+LABLE+'.txt'
#SIMILARITY = "jdr"
#LABELS_PATH2 = PATH+'SyntheticResults/'+LABLE+'/'+LABLE+'_'+SIMILARITY+'_labels_diff.txt'

LABELS1 = data_utility.read_file_labels(LABELS_PATH1)
LABELS2 = data_utility.read_file_labels(LABELS_PATH2)



matrix = comp.compare(LABELS1, LABELS2, NUMBER_OF_CLUSTERS)

#1 for greeen, 2 for red and 3 for blue- where the value is close to both clusters
m = np.zeros(shape=(len(matrix), len(matrix)))

for indx in range(0,len(matrix)):
    
    #mark green
    aIndx = matrix[indx,:].argmax() 
    
    #check if it is neighbor of the both clusters
    checkBlue = matrix[:,aIndx].argmax() 
    
    if(indx == checkBlue):
        m[indx,aIndx]=3
    else:
       m[indx,aIndx]=1 
    
    #mark red
    bIndx = matrix[:,indx].argmax()
    
    if m[bIndx,indx]==0:
        m[bIndx,indx]=2
        
orphanA =0
orphanB =0
        
for indx in range(0,len(m)):
    if not (2 in m[indx,:] or 3 in m[indx,:]):
        orphanA+=1
    if not (1 in m[:,indx] or 3 in m[:,indx]):
        orphanB+=1

CI = max(orphanA, orphanB)
print("Centroid Index: "+str(CI))
#LABLE = 'patient_dg_seq_167'
#data_1200_100_16_5_1 
#data_1200_200_4_5_1
#data_1200_200_8_5_1

#data_1200_200_16_0_1
#data_1200_200_16_5_1
#data_1200_200_16_5_2
#data_1200_200_16_5_3
#data_1200_200_16_5_4
#data_1200_200_16_5_5

#data_1200_200_16_10_1
#data_1200_200_16_20_1
#data_1200_200_16_40_1
#data_1200_400_16_5_1
#data_1200_800_16_5_1