def oddCells(m, n, indices):
    mat = []
    count = 0
    for i in range(m):
        data = []
        for j in range(n):
            data.append(0)
        mat.append(data)
    

    for row, col in indices:
        for k in range(n):
            mat[row][k] += 1
        for l in range(m):
            mat[l][col] += 1
        
    for x in range(m):
        for y in range(n):
            if mat[x][y] % 2 != 0:
                count +=1
    
    return count





print(oddCells(m = 2, n = 3, indices = [[0,1],[1,1]]))