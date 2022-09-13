"""
This module calculate Jaccard's distance score

parameters:
x : (numpy array) first string sequence
y : (numpy array) second string sequence

return:
(float) : Jaccard's distance socre (1 - Jaccard's similarlity)
"""

def jaccard_seq(x, y):
    len_x = len(x)
    len_y = len(y)
    fst, snd = (x, y) if len_x < len_y else (y, x)
    num_intersect = len(set(fst).intersection(snd))
    
    #Jaccard distance score    
    return 1-(num_intersect / (len_x + len_y - num_intersect))