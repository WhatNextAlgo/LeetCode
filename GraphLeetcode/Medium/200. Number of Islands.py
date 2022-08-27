import collections
from typing import List



class Solution:
    def numIslands1(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        no_of_islands = 0


        def dfs(i,j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] != "1":
                return
            
            grid[i][j] = "2"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    no_of_islands += 1
        return no_of_islands

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])
        no_of_islands = 0
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    rdr , cdc = row + dr,col + dc
                    if (rdr in range(rows) and
                        cdc in range(cols) and
                        grid[rdr][cdc] == "1" and 
                        (rdr,cdc) not in visit):
                        q.append((rdr,cdc))
                        visit.add((rdr,cdc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    no_of_islands += 1
        return no_of_islands

    #for iterative DFS just replace popLeft to pop






s = Solution()
print(s.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","1","1"]
]))