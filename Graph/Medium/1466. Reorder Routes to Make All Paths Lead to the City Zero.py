from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # start at city 0
        # recursively check its neighbours
        #count outgoing edges
        edges = {(u,v) for u,v in connections}
        neighbours = {city:[] for city  in range(n)}
        visit = set()
        changes = 0
        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
        
        def dfs(city):
            nonlocal edges,visit,changes

            for neighbour in neighbours[city]:
                if neighbour in visit:
                    continue
                #check if this neighbour can reach city 0
                if (neighbour,city) not in edges:
                    changes += 1
                visit.add(neighbour)
                dfs(neighbour)
        visit.add(0)
        dfs(0)
        return changes


s = Solution()
print(s.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))