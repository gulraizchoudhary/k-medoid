# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:12:44 2019

@author: gulrch
"""
import matplotlib.pyplot as plt
import numpy as np

def averageLength(data):
    summ =0
    for i in range(0, len(data)):
        summ+=len(data[i])
    return summ/len(data)

def distinctDiagnosis(data):
    dlist =dict()
    for i in range(0, len(data)):
        for l in data[i]:
            if l in dlist:
                dlist[l]+=1
            else:
                dlist[l] = 1
    #sort in descending order
    sorted_d = sorted(dlist.items() , key=lambda t : t[1] , reverse=True)
    diseases = dict()
    for k,v in sorted_d:
        diseases[k]=v

    return diseases

def sequences_lenght(data):
    dlist =dict()
    for l in data:
        if len(l) in dlist:
            dlist[len(l)]=int(dlist[len(l)])+1
        else:
            dlist[len(l)] = 1
    #sort in descending order
    sorted_d = sorted(dlist.items() , key=lambda t : t[1] , reverse=True)
    diseases = dict()
    for k,v in sorted_d:
        diseases[k]=v

    return diseases

def plot_bar(disease, RESULT_PATH, TITLE):
    x, y = disease.keys(), disease.values()
    length = int(len(x)/10)
    xi = list(range(len(x)))
    plt.bar(x,y, align="center")
    plt.xticks(np.arange(min(xi), max(xi)+1, length))
    plt.title(TITLE)
    plt.xlabel('Diseases', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.savefig(RESULT_PATH+'.png', dpi=600) 
    plt.show()
    
def plot_bar2(disease, RESULT_PATH, TITLE):
    x, y = disease.keys(), disease.values()
    plt.bar(x,y, align="center")
    #plt.xticks(np.arange(min(xi), max(xi)+1, length))
    plt.title(TITLE)
    plt.xlabel('Set Size', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.savefig(RESULT_PATH+'.png', dpi=600) 
    

def plot_bar_simple(similarity, RESULT_PATH, TITLE):
    x= range(0,len(similarity))
    y= similarity
    plt.bar(x,y, align="center")
    plt.title(TITLE)
    plt.ylabel('Distance', fontsize=12)
    plt.savefig(RESULT_PATH+'.png', dpi=600) 
    
#Plot histogram of frequent diseases in a cluster
def plot_bar_percentage(frequencies, path, title, yLabel, min, max, ylog):
    
    xlabels = frequencies.keys()
    width = 0.5
    pos1 = np.arange(len(xlabels))
    
    # gives histogram aspect to the bar diagram
    ax = plt.axes()
    ax.set_xticks(pos1)
    ax.set_xticklabels(xlabels)
    ax.set_xlabel("ICD-10")
    ax.set_ylabel(yLabel)
    ax.set_title(title)
    plt.bar(pos1, frequencies.values(), width, color='b')
    if ylog is True:
        ax.set_yscale('log')
    plt.ylim(min,max)
    plt.savefig(path+"_histogram.png", bbox_inches = "tight") # save as png
    plt.show()
    
#Plot histogram of frequent diseases in a cluster
def plot_risk_ratio(frequencies, path, title, yLabel, min, max):
    plt.rcdefaults()
    nfrequencies = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[0:10])
    objects = tuple(nfrequencies.keys())
    y_pos = np.arange(len(objects))
    performance = list(nfrequencies.values())

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    # Get the axes object
    ax = plt.gca()
    # remove the existing ticklabels
    ax.set_xticklabels([])
    # remove the extra tick on the negative bar
    ax.set_xticks([idx for (idx, x) in enumerate(performance) if x > 0])
    ax.spines["bottom"].set_position(("data", 0))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylabel(yLabel)
    ax.set_title(title)
    # placing each of the x-axis labels individually
    label_offset = 0.5
    for language, (x_position, y_position) in zip(objects, enumerate(performance)):
        if y_position > 0:
            label_y = -label_offset
        else:
            label_y = y_position - label_offset
        ax.text(x_position, label_y, language, ha="center", va="top")
    # Placing the x-axis label, note the transformation into `Axes` co-ordinates
    # previously data co-ordinates for the x ticklabels
    ax.text(0.5, -0.05, "", ha="center", va="top", transform=ax.transAxes)
    
    plt.show()

def overlap(pw_dist):
    sum =[]
    for i in range(0,len(pw_dist)):
        sum.append((np.sum(pw_dist[i])/len(pw_dist))*100)
    return sum
