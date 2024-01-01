'''
Graph Cellular Automata.
'''

import numpy as np
import random as rnd
import networkx as nx
import matplotlib.pyplot as plt

from utils import *


#-----------------------------------------------


__all__ = [
    "initial_state_in",
    "initial_state_out",
    "in_neighborhood_density",
    "out_neighborhood_density",
    "threshold_in_neighborhood",
    "threshold_out_neighborhood",
    "Run_GCA_in_neighborhood",
    "Run_GCA_out_neighborhood",
]


def initial_state_in(M):
    Seq = []
    n = len(M)
    G = nx.from_numpy_matrix(M, create_using=nx.DiGraph())
    
    for v in range(n):
        if G.in_degree(v) == 0 and G.out_degree(v) == 0:
            Seq.append(0)
        elif G.in_degree(v) != 0 and G.in_degree(v) > G.out_degree(v):
            Seq.append(1)
        else:
            Seq.append(0)
    
    return Seq


def initial_state_out(M):
    Seq = []
    n = len(M)
    G = nx.from_numpy_matrix(M, create_using=nx.DiGraph())
    
    for v in range(n):
        if G.in_degree(v) == 0 and G.out_degree(v) == 0:
            Seq.append(0)
        elif G.out_degree(v) != 0 and G.in_degree(v) < G.out_degree(v):
            Seq.append(1)
        else:
            Seq.append(0)
    
    return Seq


def in_neighborhood_density(M, v, state):
    sum_states = 0
    G = nx.from_numpy_matrix(M, create_using=nx.DiGraph())
    k_in = G.in_degree(v)
    
    for w in range(len(M)):
        sum_states += M[w, v]*state[w]
        
    if k_in != 0:
        in_density = sum_states/k_in
    else:
        in_density = 0
    return in_density


def out_neighborhood_density(M, v, state):
    sum_states = 0
    G = nx.from_numpy_matrix(M, create_using=nx.DiGraph())
    k_out = G.out_degree(v)
    
    for w in range(len(M)):
        sum_states += M[v, w]*state[w]
        
    if k_out != 0:
        out_density = sum_states/k_out
    else:
        out_density = 0
    return out_density


def threshold_in_neighborhood(M, state, th):
    S = []
    G = nx.from_numpy_matrix(M, create_using=nx.DiGraph())
    for i in range(len(M)):
        if in_neighborhood_density(M, i, state) > th:
            S.append(1 - state[i])
        else:
            S.append(state[i])
    return S


def threshold_out_neighborhood(M, state, th):
    S = []
    G = nx.from_numpy_matrix(M, create_using=nx.DiGraph())
    for i in range(len(M)):
        if out_neighborhood_density(M, i, state) > th:
            S.append(1 - state[i])
        else:
            S.append(state[i])
    return S


def Run_GCA_in_neighborhood(D, th=0.35, output="grid"):
    
    n = len(D)
    init_state = initial_state_in(D[0])
    states = [init_state]
    
    for t in range(n):
        state_t1 = threshold_in_neighborhood(D[t], states[t], th)
        states.append(state_t1)
    
    del states[0]
    
    if output == "binary":
        return np.array(states)
    
    if output == "grid":
        plt.rcParams['image.cmap'] = 'binary' #black and white grid
        fig, ax = plt.subplots(figsize=(15, 9))
        ax.matshow(states)
        ax.axis(True);

        
def Run_GCA_out_neighborhood(D, th=0.35, output="grid"):
    
    n = len(D)
    init_state = initial_state_out(D[0])
    states = [init_state]
    
    for t in range(n):
        state_t1 = threshold_out_neighborhood(D[t], states[t], th)
        states.append(state_t1)
        
    del states[0]
    
    if output == "binary":
        return np.array(states)
    
    if output == "grid":
        plt.rcParams['image.cmap'] = 'binary' #black and white grid
        fig, ax = plt.subplots(figsize=(15, 9))
        ax.matshow(states)
        ax.axis(True);
    
   