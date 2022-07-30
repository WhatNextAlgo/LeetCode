from collections import defaultdict


class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)


    def topologicalSortUtils(self,v,visited,stack):
        visited.add(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtils(i,visited,stack)
        
        stack.insert(0,v)

    def topologicalSort(self):
        visited = set()
        stack = []
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtils(k,visited,stack)

        print(stack)


g = Graph(8)

g.addEdge('A','C')
g.addEdge('B','C')
g.addEdge('B','D')
g.addEdge('D','F')
g.addEdge('C','E')
g.addEdge('E','H')
g.addEdge('E','F')
g.addEdge('F','G')

g.topologicalSort()
