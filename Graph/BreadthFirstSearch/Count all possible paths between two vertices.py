class Graph:
    def __init__(self,V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self,u,v):
        self.adj[u].append(v)

    
    def countPaths(self,s,d):
        visited = [False] * self.V
        pathCounts = [0]
        self.countPathsHelper(s,d,visited,pathCounts)
        print(pathCounts)
        print(self.adj)
        return pathCounts[0]

    def countPathsHelper(self,u,d,visited,pathCounts):
        visited[u] = True
        print(u,end=" ")
        if u == d:
            pathCounts[0] += 1
        else:
            i = 0
            while i < len(self.adj[u]):
                if not visited[self.adj[u][i]]:
                    self.countPathsHelper(self.adj[u][i],d,visited,pathCounts)

                i += 1
        visited[u] = False
        print()


# Driver Code
if __name__ == '__main__':
 
    # Create a graph given in the
    # above diagram
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)
 
    s = 2
    d = 3
    print(g.countPaths(s, d))