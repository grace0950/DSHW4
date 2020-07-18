import networkx as nx
import matplotlib.pyplot as plt

x=100
y=100
z=100


G = nx.Graph()

#{{{Graph
from collections import defaultdict 
import sys 

class Graph(): 
 
    def __init__(self, V): 
        self.V = V 
        self.graph = defaultdict(list) 
  
    def addEdge(self, src, dest, weight): 
  
        newNode = [dest, weight] 
        self.graph[src].insert(0, newNode) 
  
        newNode = [src, weight] 
        self.graph[dest].insert(0, newNode) 
  
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
  
            for pCrawl in self.graph[u]: 
                v = pCrawl[0] 
                if pCrawl[1] > 0 and sptSet[v] == False and dist[v] > dist[u] + pCrawl[1]: 
                        dist[v] = dist[u] + pCrawl[1]
        return dist[end]
#}}}

#{{{1.Generate a cycle of 1000 nodes. Each edge has length 1
for i in range(1000):
    G.add_node(i)
    if i>0:
        G.add_edge(i, i-1, len=1)

G.add_edge(0, 999, len=1)
#}}} 

#{{{initial
g = Graph(1000) 

for i in range(1,1000):
    g.addEdge(i, i-1,1)
    g.addEdge(i-1,i,1)

g.addEdge(0,999,1)
#}}}

#{{{1 2 .Add x random edges. Each random edge has the same length y.
import random

for i in range(x):
    start = random.randint(0,999)
    end = random.randint(0,999)

    G.add_edge(start, end)

    g.addEdge(start, end, y)
    g.addEdge(start, end, y)

#}}} 

#{{{Sample z pairs of source and compute the average shortest distance
"""
total = 0
for n in range(10):
    for i in range(z):
        start = random.randint(0, 999)
        end = random.randint(0, 999)
        total += g.dijkstra(start, end)

    average_d = total/(z*10)
#print("z=",z,":",average_d)
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
    print(tEnd - tStart)
#}}}

#{{{draw
plt.figure(figsize=(10,10))
nx.draw_circular(G, node_size=0.05, width=0.001)
plt.savefig("path.pdf")
#}}}
