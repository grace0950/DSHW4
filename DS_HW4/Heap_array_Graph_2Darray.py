import networkx as nx
import matplotlib.pyplot as plt

x=100
y=100
z=100


G = nx.Graph()

#{{{ 1.Generate a cycle of 1000 nodes. Each edge has length 1
for i in range(1000):
    G.add_node(i)
    if i>0:
        G.add_edge(i, i-1, len=1)

G.add_edge(0, 999, len=1)
#}}} 

#{{{class Graph()  
import sys

class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
  
        min = sys.maxsize 
  
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    def dijkstra(self, start, end): 
  
        dist = [sys.maxsize] * self.V 
        dist[start] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
  
            u = self.minDistance(dist, sptSet) 
  
            sptSet[u] = True
  
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v]
        return dist[end]
 #}}}

#{{{initialize
g = Graph(1000) 

for i in range(1,1000):
    g.graph[i][i-1]=1
    g.graph[i-1][i]=1

g.graph[0][999]=1
g.graph[999][0]=1
#}}}

#{{{ 2. Add x random edges. Each random edge has the same length y.
import random

for i in range(x):
    start = random.randint(0,999)
    end = random.randint(0,999)

    G.add_edge(start, end)

    g.graph[start][end] = y
    g.graph[end][start] = y
#}}}

#{{{Sample z pairs of source and destination and compute the average shortest distance (d)
"""
total = 0
for n in range(10):
    for i in range(z):
        start = random.randint(0, 999)
        end = random.randint(0, 999)
        total += g.dijkstra(start, end)

    average_d = total/(z*10)
#print("x=",x,":",average_d)
"""
#}}}

#{{{time
import time

for n in range(10):
    start = random.randint(0,999)
    end = random.randint(0,999)
    tStart = time.time()
    g.dijkstra(start,end)
    tEnd = time.time()
    print("No.",n,":",(tEnd - tStart))
#}}}

#{{{draw
plt.figure(figsize=(10,10))
nx.draw_circular(G, node_size=0.05, width=0.001)
plt.savefig("path.png")
#}}}
