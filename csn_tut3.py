#CSN Internal Assesment Assignment
#Pritam Chakraborty , Slno. 36, Rollno. 19079762010

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

#1oading the adjacency matrix 36.txt
ADJ = np.loadtxt("36.txt", dtype='i')

#checking the matrix
if (np.allclose(ADJ,ADJ.T, 1e-5,1e-6) == True):
    symm = 1
else:
    symm = 0


'''1.Generate the graph and save it in png format. Name it in the format
    graph_yourname_rollnumber.'''
if (symm == 1):
    G = nx.from_numpy_matrix(ADJ, create_using=nx.Graph())

else :
    G = nx.from_numpy_matrix(ADJ, create_using=nx.DiGraph())

options = {'node_size': 500,'node_color' : 'yellow', 'edge_color' : 'black'}
nx.draw_circular(G,**options,with_labels=True)
plt.savefig("graph_pritamchakraborty_19079762010.png")
plt.plot()
plt.show()


'''2. Edge list of graphGenerate and save the edge-list of your graph. Save the edge-list in a text file
which is to be named as edgelist_yourname_rollnumber'''
e_count = 0 #counter for edge list
file = open('edgelist_pritamchakraborty_19079762010.txt', 'w+')
for E in nx.generate_edgelist(G, delimiter=',',data=False):
    #print(E)
    file.write(E)
    file.write("\n")
    e_count = e_count + 1

file.close()


#q3.a What is the total number of edges in the graph?
#print("the number of edges is", e_count)
print("the number of edges is", G.number_of_edges())

#q3.b What is the average out-degree?
deg = [d for n, d in G.degree()]
#print("degrees",deg)

avg_deg = sum(deg)/(G.order()) #average degree
print("average degree", avg_deg)

#print("sum", np.sum(ADJ))


#4.a What is the largest in-degree?
print("the maximum value of degree is ", max(deg))

#4.b. List the node(s) with the largest in-degree.
for n in G.nodes():
    if (G.degree[n] == max(deg)): #checks the degree of the nth node with max degree
        print("node with degree",G.degree([n]))


#5. Generate the degree distribution
import collections

degCnt = collections.Counter(sorted([d for n, d in G.degree()], reverse=True))
#print(degCnt)
k, nk = zip(*degCnt.items())
prd = np.divide(nk, len(G.nodes()))

print("degree distribution")
print("k\tn(k)\tp(k)")
for n in range(0,len(degCnt)):
    print(k[n],'\t',nk[n],'\t',prd[n])

plt.title("degree distribution p(k)-k plot")
plt.xlabel("k")
plt.ylabel("p(k)")
plt.plot(k, prd,c='r',marker='^')
plt.savefig("degdist_pritamchakraborty_19079762010.png")
plt.show()


#6.What is the diameter of the graph?
print("Diameter of the graph is",nx.diameter(G))


#7. What is the average path length of the graph?
''' i've used the formula
    avg path length or a = summation d(i,j)/n(n-1)
    here, summation done over s,t in set of nodes
    ,i&j node index and n is total number of nodes
'''
print("average shortest path length", nx.average_shortest_path_length(G))


#8. How many distinct walks of length two exist in the graph (excluding closed walks)?
A_sq = np.dot(ADJ,ADJ)
'''n_wk2 = 0
for i in range(G.order()):
    for j in range(G.order()):
        if (i != j):
            n_wk2 = n_wk2 + A_sq[i][j]
'''
print("the number of walks of length 2 excluding closed walks", (np.sum(A_sq)-np.trace(A_sq)))


#9. How many distinct closed walks of length three exist in the graph from node 3 to node 5?
A_cb = np.dot(ADJ,A_sq)
print("the number of distinct walks of length 3 from node labelled 3 to node labelled 5",A_cb[3][5])


'''10. If your graph is directed, identify the size and the nodes belonging to the
largest strongly connected component of the graph; else, if your graph is
undirected, find the size and the nodes belonging to the largest connected
component.'''
lar_cc = max(nx.connected_components(G), key=len)
print("The largest connected component of undirected graph:", lar_cc)
print("size",len(lar_cc))


#11. Which node has the highest “betweenness centrality” and what is it?
n=G.order()
bet_cent=nx.betweenness_centrality(G,normalized=False) #gives a dictionary a nodes and between centrality measure
#print(bet_cent)
nn = [ ]   #creates a null list to store node values
blist = [ ]   #null list to store centrality value
#print('normalized according to class :\n')
for key, value in bet_cent.items():
    #print(key, '->',(1/n**2)*value)
    blist.append((1/n**2)*value)  #renormalisation is applied
    nn.append(key)

#print(len(bet_cent),len(nn))
for i in range(len(nn)):
    if (blist[i] == max(blist)):
        print("node having the maximum centrality",nn[i])


'''12. In the undirected/associated undirected graph, what is the average
clustering coefficient of the graph? (if a node has a degree less than 2, take
its clustering coefficient to be zero)'''
print("average clustering coefficient", nx.average_clustering(G,count_zeros=True)) #here we have included nodes with zero clustering coefficient


'''13. In the case of undirected/associated undirected graph, does there exist a
cycle? If yes, how many cycles exist in the undIrected/associated undirected
graph? What is the size of the longest cycle?'''
print("number of cycles",len(nx.cycle_basis(G)))

all_cycles = list(nx.cycle_basis(G)) # list of cycles stored in all_cycles
answer = [ ] # empty array
longest_cycle_len = 0
for cycle in all_cycles: # for loop to go through each cycle in the list
    cycle_len = len(cycle)
    if cycle_len>longest_cycle_len:
        answer =cycle
        longest_cycle_len = cycle_len

print("Longest Cycle is {} with length {}.".format(answer,longest_cycle_len))


'''14. In the undirected/Associated undirected graph, how many nodes are at a
distance two from node 5 (excluding the node 5 itself)?'''
node_distnc = nx.single_source_shortest_path_length(G,5,cutoff=2) #generates a dictionery of nodes & distance having distance <= 2

count = 0
for node in node_distnc:
    #print(f"{node}: {node_distnc[node]}")
    if (node_distnc[node]==2):
        count = count + 1

print("number of nodes",count)

'''n2 = 0
for i in range(len(G.nodes())):
    d = nx.shortest_path(G,5,i)
    if ((len(d)-1)==2 and (i!=5)):
        n2 = n2 +1

print("no fo nodes",n2 )'''

'''15. How would you characterize your graph? ‘Erdos-Renyi’, ‘small-world ’,
‘scale-free’ or ‘regular’? Give reasons. Is the categorization clear or could it
fall into multiple categories?'''

'''
    based on the values of:
    avg clustering coefficient ~ 0.3347
    diameter ~6
    it is an Erdos Reiyni
    
    however looking at the degree distribution we can deduce that for higher degree values
    there isnt much nodes , so its a small-world
'''