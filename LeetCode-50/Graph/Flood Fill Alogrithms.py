from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(grid, i, j, old_color, new_color) -> None:
            n = len(grid)
            m = len(grid[0])
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != old_color:
                return
            else:
                grid[i][j] = new_color
                dfs(grid, i+1, j, old_color, new_color)
                dfs(grid, i-1, j, old_color, new_color)
                dfs(grid, i, j+1, old_color, new_color)
                dfs(grid, i, j-1, old_color, new_color)

        def flood_fill(grid, i, j, new_color) -> None:
            old_color = grid[i][j]
            if old_color == new_color:
                return
            dfs(grid, i, j, old_color, new_color)

        flood_fill(image,sr,sc,color)

        return image



s= Solution()
print(s.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))

# DFS approach:
def dfs(grid, i, j, old_color, new_color):
    n = len(grid)
    m = len(grid[0])
    if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != old_color:
        return
    else:
        grid[i][j] = new_color
        dfs(grid, i+1, j, old_color, new_color)
        dfs(grid, i-1, j, old_color, new_color)
        dfs(grid, i, j+1, old_color, new_color)
        dfs(grid, i, j-1, old_color, new_color)

def flood_fill(grid, i, j, new_color):
    old_color = grid[i][j]
    if old_color == new_color:
        return
    dfs(grid, i, j, old_color, new_color)

    
 
# BFS approach:
from queue import Queue

def flood_fill(grid, i, j, new_color):
    n = len(grid)
    m = len(grid[0])
    old_color = grid[i][j]
    if old_color == new_color:
        return
    queue = Queue()
    queue.put((i, j))
    count = 0
    while not queue.empty():
        i, j = queue.get()
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != old_color:
            continue
        else:
            grid[i][j] = new_color
            queue.put((i+1, j))
            queue.put((i-1, j))
            queue.put((i, j+1))
            queue.put((i, j-1))
        count += 1
    return count 


print(flood_fill(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
],i =0,j = 0,new_color = 1))