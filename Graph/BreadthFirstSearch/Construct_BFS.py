from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    
    def addEdge(self,src,dest):
        self.graph[src].append(dest)

    
    def bfs(self,s):
        visited = set()
        q = []
        q.append(s)
        visited.add(s)
        while q != []:
            dequeued = q.pop(0)
            print(dequeued, end = " ")
            for  neighbour in self.graph[dequeued]:
                if neighbour not in visited:
                    q.append(neighbour)
                    visited.add(neighbour)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.bfs(2)
