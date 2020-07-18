import networkx as nx
import matplotlib.pyplot as plt

x=100
y=100
z=100


G = nx.Graph()

#{{{Heap
from collections import defaultdict 
import sys 
  
class Heap(): 
  
    def __init__(self): 
        self.array = [] 
        self.size = 0
        self.pos = [] 
  
    def newMinHeapNode(self, v, dist): 
        minHeapNode = [v, dist] 
        return minHeapNode 
  
    # A utility function to swap two nodes  
    # of min heap. Needed for min heapify 
    def swapMinHeapNode(self,a, b): 
        t = self.array[a] 
        self.array[a] = self.array[b] 
        self.array[b] = t 
  
    # A standard function to heapify at given idx 
    # This function also updates position of nodes  
    # when they are swapped.Position is needed  
    # for decreaseKey() 
    def minHeapify(self, idx): 
        smallest = idx 
        left = 2*idx + 1
        right = 2*idx + 2
  
        if left < self.size and self.array[left][1] < self.array[smallest][1]: 
            smallest = left 
  
        if right < self.size and self.array[right][1] < self.array[smallest][1]: 
            smallest = right 
  
        # The nodes to be swapped in min  
        # heap if idx is not smallest 
        if smallest != idx: 
  
            # Swap positions 
            self.pos[ self.array[smallest][0] ] = idx 
            self.pos[ self.array[idx][0] ] = smallest 
  
            # Swap nodes 
            self.swapMinHeapNode(smallest, idx) 
  
            self.minHeapify(smallest)

    # Standard function to extract minimum  
    # node from heap 
    def extractMin(self): 
  
        # Return NULL wif heap is empty 
        if self.isEmpty() == True: 
            return
  
        # Store the root node 
        root = self.array[0] 
  
        # Replace root node with last node 
        lastNode = self.array[self.size - 1] 
        self.array[0] = lastNode 
  
        # Update position of last node 
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
  
        # Reduce heap size and heapify root 
        self.size -= 1
        self.minHeapify(0) 
  
        return root 
  
    def isEmpty(self): 
        return True if self.size == 0 else False
  
    def decreaseKey(self, v, dist): 
  
        # Get the index of v in  heap array 
  
        i = self.pos[v] 
  
        # Get the node and update its dist value 
        self.array[i][1] = dist 
  
        # Travel up while the complete tree is  
        # not hepified. This is a O(Logn) loop 
        while i > 0 and self.array[i][1] < self.array[int((i - 1) / 2)][1]: 
  
            # Swap this node with its parent 
            self.pos[ self.array[i][0] ] = int((i-1)/2)
            self.pos[ self.array[int((i-1)/2)][0] ] = i 
            self.swapMinHeapNode(i, int((i - 1)/2) ) 
  
            # move to parent index 
            i = int((i - 1) / 2); 
  
    # A utility function to check if a given  
    # vertex 'v' is in min heap or not 
    def isInMinHeap(self, v): 
  
        if self.pos[v] < self.size: 
            return True
        return False
  
#}}}

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
  
    def dijkstra(self, src, end): 
  
        V = self.V  # Get the number of vertices in graph 
        dist = []   # dist values used to pick minimum  
                    # weight edge in cut 
  
        minHeap = Heap() 
  
        for v in range(V): 
            dist.append(sys.maxsize) 
            minHeap.array.append( minHeap.newMinHeapNode(v, dist[v]) ) 
            minHeap.pos.append(v) 
  
        minHeap.pos[src] = src 
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src]) 
  
        minHeap.size = V; 
  
        while minHeap.isEmpty() == False: 
  
            newHeapNode = minHeap.extractMin() 
            u = newHeapNode[0]

            for v in range(self.V): 
  
                if self.graph[u][v] > 0 and minHeap.isInMinHeap(v) and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = self.graph[u][v] + dist[u] 
  
                        minHeap.decreaseKey(v, dist[v])

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
    print(tEnd - tStart)
#}}}

#{{{draw
plt.figure(figsize=(10,10))
nx.draw_circular(G, node_size=0.05, width=0.001)
plt.savefig("path.pdf")
#}}}
