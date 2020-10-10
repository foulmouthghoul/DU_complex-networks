#9/10/2020 - tutorial 1 - question 5

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from functools import reduce

#1oading the adjacency matrix ADJ.txt and converring into directed graph
ADJ = np.loadtxt("ADJ.txt", dtype='i')
Gd = nx.from_numpy_matrix(ADJ,create_using = nx.DiGraph())

nx.draw_circular(Gd, with_labels=True) #for our convience
plt.show()

""" to find the number of nodes of a graph we need to find
    the number of elements in a row or column
    in the adjacency matrix ADJ
"""
n_nodes = len(ADJ) #n_nodes gives the number of nodes
print(n_nodes)

nnode = Gd.order() #however the network package documentation had better inbuilt functions
print(nnode)

#we use inbulit library fucntions from the networkx package
#for calculating degree of the nodes
i_deg = list(Gd.in_degree())
print("in degrees",i_deg)

o_deg = list(Gd.out_degree())
print("out degrees",o_deg)

#calculation of average in degree
avg_ideg = 0

ext_ideg = list
ext_ideg = reduce(np.append, i_deg) #extracting the elements from tuple i_deg
for i in range(0, len(i_deg)):
    avg_ideg = avg_ideg + int(ext_ideg[(i+1)])

print("average in degree",avg_ideg)

#calculation of average out degree
avg_odeg = 0

ext_odeg = list
ext_odeg = reduce(np.append, o_deg) #extracting the elements from tuple o_deg
for i in range(0, len(o_deg)):
    avg_odeg = avg_odeg + int(ext_odeg[(i+1)])

print("average out degree", avg_odeg)

if avg_ideg == avg_odeg:
    print("They are same")
else:
    print("They are not same")