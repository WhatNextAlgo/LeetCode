from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    
    def addEdge(self,src,dest):
        self.graph[src].append(dest)

    def dfs(self,s):
        visited = set()
        self.dfs_helper(s,visited)

    def dfs_helper(self,s,visited):
        visited.add(s)
        print(s,end=" ")
        for neighbour in self.graph[s]:
            if neighbour not in visited:
                self.dfs_helper(neighbour,visited)
    
    def path_from_each_vertex(self):
            visited = set()
            for vertex in self.graph:
                if vertex not in visited:
                    self.dfs_helper(vertex,visited)
                    print()
                


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Depth First Traversal"
                  " (starting from vertex 2)")
#g.dfs(2)
g.path_from_each_vertex()
