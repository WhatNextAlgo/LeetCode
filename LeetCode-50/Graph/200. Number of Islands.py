def dfs(grid, i, j,n, m) -> None:
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] !="1":
            return
        else:
            grid[i][j] = "2"
            dfs(grid, i+1, j,n, m)
            dfs(grid, i-1, j,n, m)
            dfs(grid, i, j+1,n, m)
            dfs(grid, i, j-1,n, m)

def no_of_islands(grid) -> int:
    n = len(grid)
    m = len(grid[0])
    no_of_island = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y] == "1":
                dfs(grid,x,y,n,m)
                no_of_island += 1

    return no_of_island
   


print(no_of_islands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
