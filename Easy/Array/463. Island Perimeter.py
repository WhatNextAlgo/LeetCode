from typing import List

def islandPerimeter(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for i in range(rows):
        corner = 0
        for j in range(cols):
            if i==0:
                if grid[i][j]==1:
                    count += 4
                    if corner == 1:
                        count -=2
                    corner = 1
                else:
                    corner = 0
            else:
                if grid[i][j]==1:
                    count += 4
                    if corner == 1:
                        count -= 2
                    if grid[i-1][j]==1:
                        count -= 2
                    corner = 1
                else:
                    corner = 0
    return count        
                    
print(islandPerimeter(grid = [[1,1]]))