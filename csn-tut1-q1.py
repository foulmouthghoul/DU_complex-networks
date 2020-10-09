# 9/10/2020 - question 1 2 & 3
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# nodes
N = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
file = open("nodes_list.txt", 'w+')
np.savetxt("nodes_list.txt", N, fmt='%s')

# edges
E = np.array([(1, 2), (1, 3), (3, 4), (6, 7), (10, 1), (10, 9)])
file = open("edges_list.txt", 'w+')
np.savetxt("edges_list.txt", E, fmt='%s')

G = nx.DiGraph()
G.add_nodes_from(N)
G.add_edges_from(E)

#adding graph attributes
options = {'node_color': 'yellow','node_size': 1000,'edge_color': 'blue'}
nx.draw_circular(G, **options, with_labels=True)

plt.savefig("GRAPH_1.png")
plt.plot()
plt.show()

