class Graph:
    def __init__(self,graph = None):
        if graph is None:
            self.graph = {}
        self.graph = graph

    def bfs(self,start,end):
        queue = []
        queue.append(start)

        while queue  != []:
            print(queue)
            path = queue.pop(0)
            node = path[-1]
            print("node : ",node)
            if node == end:
                return path
            for adjacent in self.graph.get(node,[]):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


cd = { "a":["b","c"],
        "b":["d","g"],
        "c" :["d","e"],
        "d":["f"],
        "e" :["f"],
        "g" :["f"]

}

g = Graph(cd)
print(g.bfs("a","f"))

