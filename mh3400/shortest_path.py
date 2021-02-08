from random import randint
import math
import networkx as nx
import matplotlib.pyplot as plt

NODES = 8              # defines number of nodes in the graph
EDGES = 20              # defines number of edges in the graph
DIRECTED = True         # defines if the graph is directed or undirected
NEGATIVE_WEIGHT = False # defines if the edges can have negative weight
INFINITY = math.inf     # defines a variable for infinity


# function that implements the Dijkstra's algorithm for single-pair shortest paths
def dijkstra(graph, start_node):
    D = [INFINITY]*len(graph)
    D[start_node] = 0                           # set the start_node distance to be 0 as the distance to itself is just 0
    node = start_node                           # set node to be the start_node
    visited = [start_node]                      # create a vector visited to store the nodes that have been traversed

    for i in range(len(graph)):                 # n iterations
        for j in range(len(graph[node])):       # go through the connected nodes of the node
            vertex = graph[node][j][0]          # set the connected nodes to be vertex
            weight = graph[node][j][1]          # and the weights of the edges of the connected nodes to be weight
            if D[node] + weight < D[vertex]:    # if the distance of the node + the weight is less than the distance of the the vertex
                D[vertex] = D[node] + weight    # update the distance of the vertex because the goal is to find the shortest path
                
        neighbours = []                         # create a vector neighbours to store the nodes that dont have infinity distance
        for k in D:                             # go through the elements in D
            if k > 0 and k < 10000:             # if the element is positive and less than infinity (set to be a very large number here)
                neighbours.append(k)            # add them to neighbours
        neighbours = sorted(neighbours)         # sort the vector neighbours to obtain the next smallest element
        for l in neighbours:                    # go through the elements in neighbours
            if D.index(l) not in visited:       # if the index of l in D (the corresponding vertex) has not yet been visited
                node = D.index(l)               # update node to be the vertex
                visited.append(node)            # add the vertex to visited
                break                           # break the loop here as the next smallest element has been found
        
    return D
    

# function that implements the Floyd-Warshall's algorithm for all-pairs shortest paths
def floyd_warshall(graph):
    D = [[[ INFINITY for i in range(len(graph)) ] for j in range(len(graph)) ] for k in range(len(graph)+1) ]
   
    #initialization
    for i in range(len(graph)):                 # go through all nodes in the graph
        D[0][i][i] = 0                          # set the distance to be zero as the distance of a node to itself is just 0
        for j in range(len(graph[i])):          # go through the connected nodes of the node
            vertex = graph[i][j][0]             # set the connected nodes to be vertex
            weight = graph[i][j][1]             # and the weights of the edges of the connected nodes to be weight
            D[0][i][vertex] = weight            # the distance of the vertex is just the weight 
    
    #recursion performed n times using the recursive formula
    for k in range(1,len(graph)+1):
        for i in range(len(graph)):
            for j in range(len(graph)):
                D[k][i][j] = min(D[k-1][i][j],D[k-1][i][k-1]+D[k-1][k-1][j])
                # take the minimum of the current value and another possible route

    return D[len(graph)][:][:]

    
# function that creates the graph
def make_graph(NUMBER_NODES, NUMBER_EDGES, NEGATIVE_WEIGHT, DIRECTED):
    if NODES*NODES<NUMBER_EDGES: 
        print("Impossible to generate a simple graph with %i nodes and %i edges!\n" %(NUMBER_NODES,NUMBER_EDGES))
        return None
    g = [[] for i in range(NUMBER_NODES)]
    for i in range(NUMBER_EDGES):
        while True:
            start_node = randint(0,NUMBER_NODES-1)
            end_node = randint(0,NUMBER_NODES-1)
            if NEGATIVE_WEIGHT: weight = randint(-20,20)
            else: weight = randint(1,20)
            if (start_node != end_node): 
                found = False
                for j in range(len(g[start_node])): 
                    if g[start_node][j][0] == end_node: found = True
                if not found: break            
        g[start_node].append([end_node, weight])
        if DIRECTED==False: g[end_node].append([start_node, weight])
    return g
 

# function that prints the graph
def print_graph(g, DIRECTED):
    if DIRECTED: G = nx.DiGraph()
    else: G = nx.Graph()
    for i in range(len(g)): G.add_node(i)
    for i in range(len(g)):
        for j in range(len(g[i])): G.add_edge(i,g[i][j][0],weight=g[i][j][1])
    for i in range(len(g)):
        print("from node %02i: " %(i),end="")
        print(g[i])
    pos = nx.spring_layout(G)
    nx.draw(G,pos, with_labels=True)
    if DIRECTED: 
        labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels, label_pos=0.3)
    else:
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)



    
print("\n\n ******** GENERATING GRAPH ********" )     
g = make_graph(NODES,EDGES,NEGATIVE_WEIGHT,DIRECTED)
if g==None: raise SystemExit(0)
elif NODES<50 and EDGES<2500:
    plt.figure(1)
    print_graph(g,DIRECTED)

print("\n\n ******** PERFORMING DIJKSTRA ********" )    
D = dijkstra(g,0)
print("Single-Pair Distance Table (from node 0): ",end="")
print(D)

print("\n\n ******** PERFORMING FLOYD WARSHALL ********" )   
D = floyd_warshall(g)
print("All-Pairs Distance Table: \n",end="")
for i in range(len(g)): 
    print("from node %02i: " %(i),end="")
    print(D[i])
