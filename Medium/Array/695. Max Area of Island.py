from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j,n, m,no_of_island) -> None:
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] !=1:
                return
            else:
                grid[i][j] = 2
                no_of_island[0] += 1
                dfs(grid, i+1, j,n, m,no_of_island)
                dfs(grid, i-1, j,n, m,no_of_island)
                dfs(grid, i, j+1,n, m,no_of_island)
                dfs(grid, i, j-1,n, m,no_of_island)

        def no_of_islands(grid) -> int:
            n = len(grid)
            m = len(grid[0])
            
            max_area = 0
            for x in range(n):
                for y in range(m):
                    if grid[x][y] == 1:
                        no_of_island = [0]
                        dfs(grid,x,y,n,m,no_of_island)
                        if max_area < no_of_island[0]:
                            max_area = no_of_island[0]


            return max_area
        return no_of_islands(grid)

s = Solution()
print(s.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(s.maxAreaOfIsland(grid = [[0,0,0,0,0,0,0,0]]))