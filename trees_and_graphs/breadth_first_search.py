import os
from collections import deque

class Node:
    def __init__ (self, data):
        self.data = data
        self.edges = []

class Graph:
    def __init__ (self, nodes = []):
        self.nodes = nodes
    
    def addNode (self, val):
        node = Node (val)
        self.nodes.append (node)
    
    def addEdge (self, node1, node2):
        node1.edges.append(node2)
        node2.edges.append (node1)

    def bfs (self):
        if self.nodes is []:
            return None
        
        start = self.nodes[0]
        visited, queue, result = set([start]), deque([start]), []

        while queue:
            node = queue.popleft()
            result.append (node)
            for n in node.edges:
                if n not in visited:
                    queue.append (n)
                    visited.add (n)
            
        return result
                
graph = Graph ()
graph.addNode(5)
graph.addNode(10)
graph.addNode (15)
graph.addNode (1)
graph.addNode (20)
graph.addNode (25)
graph.addNode (30)

graph.addEdge (graph.nodes[0], graph.nodes[1])
graph.addEdge (graph.nodes [1], graph.nodes[2])
graph.addEdge (graph.nodes [2], graph.nodes[3])
graph.addEdge (graph.nodes [2], graph.nodes[4])
graph.addEdge (graph.nodes [3], graph.nodes[5])
graph.addEdge (graph.nodes [1], graph.nodes[6])
graph.addEdge (graph.nodes [0], graph.nodes[2])

bfs = graph.bfs()

for b in bfs:
    print (b.data)