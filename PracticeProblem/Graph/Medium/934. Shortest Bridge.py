from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit =set()

        def invalid(r,c):
            return r < 0 or c < 0 or r >= N or c >= N

        def dfs(r,c):
            if (invalid(r,c) or not grid[r][c] or (r,c) in visit):
                return
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r + dr,c + dc)

        def bfs():
            res = 0
            q = deque(visit)
            while q:
                for _ in range(len(q)):
                    r , c = q.popleft()
                    for dr, dc in directions:
                        curR, curC = r + dr, c + dc
                        if (invalid(curR,curC) or (curR,curC) in visit):
                            continue

                        if grid[curR][curC]:
                            return res
                        q.append([curR,curC])
                        visit.add((curR,curC))
                res += 1
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()




s = Solution()
print(s.shortestBridge(grid = [[0,1],[1,0]]))
print(s.shortestBridge(grid = [[0,1,0],[0,0,0],[0,0,1]]))
print(s.shortestBridge(grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))