from typing import List


class Solution:
    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        max_area = 0

        def dfs(r,c,island):
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or
                grid[r][c] != 1):
                return 

            grid[r][c] =2
            island[0] += 1

            dfs(r + 1,c , island)
            dfs(r - 1,c , island)
            dfs(r ,c + 1, island)
            dfs(r ,c - 1, island)

        for r in range(ROWS):
            for c in range(COLS):
                island= [0]
                if grid[r][c] == 1:
                    dfs(r,c,island)
                    max_area = max(max_area,island[0])

        return max_area

    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        visit = set()
        max_area = 0

        def dfs(r,c):
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or
                (r,c) in visit or
                grid[r][c] == 0 ):
                return 0

            visit.add((r,c))
            return (1 + dfs(r + 1,c) +
                        dfs(r - 1,c) +
                        dfs(r,c + 1) +
                        dfs(r ,c - 1))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    
                    max_area = max(max_area,dfs(r,c))

        return max_area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        max_area = 0

        def dfs(r,c):
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or
                grid[r][c] != 1 ):
                return 0

            grid[r][c] = 2
            return (1 + dfs(r + 1,c) +
                        dfs(r - 1,c) +
                        dfs(r,c + 1) +
                        dfs(r ,c - 1))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area,dfs(r,c))

        return max_area
            



s = Solution()
print(s.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                [0,0,0,0,0,0,0,1,1,0,0,0,0]]))