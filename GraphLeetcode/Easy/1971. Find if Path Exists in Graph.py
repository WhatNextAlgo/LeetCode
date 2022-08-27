from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for u,v in edges:   
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        q = [source]
        visit.add(source)
        while q != []:
            node = q.pop(0)
            if node == destination:
                return True
            
            for nei in adj[node]:
                if nei not in visit:
                    q.append(nei)
                    visit.add(nei)
        return False

s = Solution()
print(s.validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5))
print(s.validPath(n=10,edges=[[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]],source=7,destination=5))        
        