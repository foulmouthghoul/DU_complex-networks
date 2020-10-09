#9/10/2020 - tutorial 1 - question 4

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

#1oading the adjacency matrix ADJ.txt
ADJ = np.loadtxt("ADJ.txt", dtype='i')

#creating directed graph
Gdi = nx.from_numpy_matrix(ADJ,create_using=nx.DiGraph())

#creating undirected graph from directed graph Gdi
Gun = nx.to_undirected(Gdi)

#adding graph attributes
options = {'node_color': 'yellow','node_size': 1000,'edge_color': 'blue'}
nx.draw_circular(Gdi, **options, with_labels=True)

plt.savefig("DirectedGraph.png")
plt.plot()
plt.show()

nx.draw_circular(Gun,**options, with_labels=True)
plt.savefig("UndirectedGraph.png")
plt.plot()
plt.show()

#accessing nodes and edges
node = Gdi.nodes.data()
file = open('node-q4.txt', 'w+')
np.savetxt('node-q4.txt', node, fmt='%s')

edge = Gdi.edges.data()
edge = str(edge)
with open('edge-q4.txt', 'w+') as file:
    file.write(edge)
