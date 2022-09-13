# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:22:12 2019

@author: gulrch
"""


# Dynamic Programming implementation of LCS problem 
def lcs(x,y):
    m=len(x)
    n=len(y)

    #Syntax is column*rows for memoization table for m*n matrix
    L=[[None]*(n+1) for i in range(m+1)]
    
    #Loop over the memoization table
    for i in range(m+1):
        for j in range(n+1):
            #Initializing first row and cloumn of memoization table
            if i == 0 or j == 0:
                L[i][j]=0
            #Diagonal condtion if equal
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            #Diagonal if value is not equal
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    
    #The final resullt
    return L[m][n]
# end of function lcs 

def lcs_length(a, b):
    table = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i, ca in enumerate(a, 1):
        for j, cb in enumerate(b, 1):
            table[i][j] = (
                table[i - 1][j - 1] + 1 if ca == cb else
                max(table[i][j - 1], table[i - 1][j]))
    return table[-1][-1]


def lcsubstring_length(a, b):
    table = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    l = 0
    for i, ca in enumerate(a, 1):
        for j, cb in enumerate(b, 1):
            if ca == cb:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > l:
                    l = table[i][j]
    return l