from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        vist =set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 1
            if (r,c) in vist:
                return 0

            vist.add((r,c))
            perim = dfs(r,c + 1)
            perim += dfs(r + 1 ,c)
            perim += dfs(r,c - 1)
            perim += dfs(r - 1,c)

            return perim

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return dfs(r,c)


s = Solution()
print(s.islandPerimeter(grid = [[0,1]]))
