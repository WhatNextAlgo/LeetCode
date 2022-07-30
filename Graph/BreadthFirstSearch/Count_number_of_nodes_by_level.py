


adj = [[]  for _ in range(100)]

def addEdge(v,w):
    adj[v].append(w)
    adj[w].append(v)

def bfs(s,l):
    V = 100
    visited = [False] * V
    level = [0] * V
    for i in range(V):
        visited[i] =False
        level[i] = 0

    queue = []
    visited[s] = True
    queue.append(s)
    level[s] = 0
    while queue != []:
        dequeued = queue.pop(0)

        for i in adj[dequeued]:
            if not visited[i]:
                level[i] = level[dequeued] + 1
                visited[i] = True
                queue.append(i)

    count = 0
    print(level)
    for i in range(V):
        if (level[i] == l):
            count += 1

    return count

if __name__ == '__main__':
     
    # Create a graph given
    # in the above diagram
    addEdge(0, 1)
    addEdge(0, 2)
    addEdge(1, 3)
    addEdge(2, 4)
    addEdge(2, 5)
  
    level = 2
  
    print(bfs(0, level))