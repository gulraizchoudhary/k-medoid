# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:54:31 2019

@author: gulrch
"""

#This implementation is based on strsim library in python
#-The library also contains the many other similarity measures such as edit distance etc. 
#https://pypi.org/project/strsim/#optimal-string-alignment

#Longest Common Subsequence
#The longest common subsequence (LCS) problem consists in finding the longest subsequence common to two (or more) sequences. 
#It differs from problems of finding common substrings: unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences.
#
#It is used by the diff utility, by Git for reconciling multiple changes, etc.

#The LCS distance between strings X (of length n) and Y (of length m) is n + m - 2 |LCS(X, Y)| min = 0 max = n + m

def lcss(t0, t1):
    """
    Usage
    -----
    The Longuest-Common-Subsequence distance between trajectory t0 and t1.
    Parameters
    ----------
    param t0 : len(t0)x2 numpy_array
    param t1 : len(t1)x2 numpy_array
    Returns
    -------
    lcss : float
           The Longuest-Common-Subsequence distance between trajectory t0 and t1
    """
    n0 = len(t0)
    n1 = len(t1)
    # An (m+1) times (n+1) matrix
    C = [[0] * (n1+1) for _ in range(n0+1)]
    for i in range(1, n0+1):
        for j in range(1, n1+1):
            if t0[i-1]==t1[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C[n0][n1]