# 13/10/2020 - tutorial 1 - question 5

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

#1oading the adjacency matrix ADJ.txt and converring into directed graph
ADJ = np.loadtxt("ADJ.txt", dtype='i')
Gu = nx.from_numpy_matrix(ADJ,create_using = nx.Graph())

nx.draw_circular(Gu, with_labels=True) #for our convience
plt.show()

# calculating the number of nodes
n_node = Gu.order() #however the network package documentation had better inbuilt functions
print("number of nodes", n_node)

#we use inbulit library fucntions from the networkx package
#for calculating degree of the nodes
t_deg = [d for n, d in Gu.degree()]
print("degrees",t_deg)

# calculating average degree of the given graph
''' for a undirected graph the average degree is the
    avg = 2 * sum of degree / number of nodes
'''
avg_deg = sum(t_deg)/n_node #average in degree
print("average in degree", avg_deg)

''' the number of walks of length k is given by,
    summation (A^k)ij
    where A is the adjacency matrix
'''
A = nx.to_numpy_matrix(Gu) # converting fro undirected graph
print("adjacent mat")
print(A)

# for lenght two we need to square the ADJ
A_sq = np.dot(A,A)
print("sqaure of A")
print(A_sq)
#print("the number of distinct walks of length 2 from node labelled 3 to node labelled 7",A_sq[3][7])
#print("the number of distinct walks of length 2 from node labelled 7 to node labelled 3",A_sq[7][3])

# looking at the graph we find from 3 to 7 there are 0
# from 7 to 3 there are 2 , 7-4-3 & 7-1-3

A_cube = np.dot(A,A_sq)
print("cube of A")
print(A_cube)

# for closed walk end adn opening vertices should be same
# so including them would be sum of all elements in (A^3) matrix
print("the number of walks of lenght 3 including closed walks", np.sum(A_cube))

# for excluding closed walks we perform index wise calculation
n_wk3 = 0

for i in range(n_node):
    for j in range(n_node):
        if (i != j):
            n_wk3 = n_wk3 + int(A_cube[i][j])

print("the number of walks of length 3 excluding closed walks", n_wk3)