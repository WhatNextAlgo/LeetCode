import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1 , y1 = points[i]
            for j in range(i + 1,N):
                x2,y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        #Prim's Algo
        res = 0
        visit = set()
        minH = [[0,0]] # [Cost,Dist]
        while len(visit) <N:
            cost , i = heapq.heappop(minH)
            if i in visit:
                continue

            res += cost
            visit.add(i)
            for neiCost,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH,[neiCost,nei])

        return res
                    
     

s = Solution()
print(s.minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))