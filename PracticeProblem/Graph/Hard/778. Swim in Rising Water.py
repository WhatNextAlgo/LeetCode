import heapq
from typing import List

#Dijkstra's Algorithms
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [[grid[0][0],0,0]] # (time/max-height,r,c)
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r ==  N - 1 and c == N -1: # destination
                return t

            for dr, dc in directions:
                neiR,neiC = r + dr, c + dc
                if neiR < 0 or neiR >= N or neiC <0 or neiC >= N or (neiR,neiC) in visit:
                    continue

                visit.add((neiR,neiC))
                heapq.heappush(minHeap,[max(t,grid[neiR][neiC]),neiR,neiC])




s = Solution()
print(s.swimInWater(grid = [[0,2],[1,3]]))
print(s.swimInWater(grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))