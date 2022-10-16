from collections import deque
from typing import List


class Solution:
    def numIslands1(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        no_of_islands = 0

        def dfs(r,c):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] != "1"):
                return 

            grid[r][c] = "2"

            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r ,c + 1)
            dfs(r ,c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    no_of_islands += 1

        return no_of_islands

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS,COLS = len(grid),len(grid[0])
        no_of_islands = 0
        visit = set()

        def bfs(r,c):

            q = deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft() # if change to popleft to pop then it will become dfs
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr , dc in directions:
                    r , c = row + dr , col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == "1" and 
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    no_of_islands += 1

        return no_of_islands



s = Solution()
print(s.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))