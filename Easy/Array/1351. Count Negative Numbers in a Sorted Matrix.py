def countNegatives(grid):
    count = 0
    for x in grid:
        for y in x:
            if y < 0:
                count +=1
    return count 

def countNegatives1(grid):
    return sum([1 for x in grid for y in x if y < 0])
    
    



print(countNegatives1(grid =[[3,2],[1,0]]))