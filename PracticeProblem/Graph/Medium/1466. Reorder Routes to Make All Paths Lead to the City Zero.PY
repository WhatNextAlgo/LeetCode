from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # start at city 0
        # recursively check its neighbours
        #count outgoing edges
        edges = {(u,v) for u,v in connections}
        neighbors = {city:[] for city in range(n)}
        visit = set()
        changes =0
        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(city):
            nonlocal edges,visit,changes

            for nei in neighbors[city]:
                if nei in visit:
                    continue
                if (nei,city) not in edges:
                    changes += 1
                visit.add(nei)
                dfs(nei)

        visit.add(0)
        dfs(0)
        return changes


s = Solution()
print(s.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))
print(s.minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]))
print(s.minReorder(n = 3, connections = [[1,0],[2,0]]))