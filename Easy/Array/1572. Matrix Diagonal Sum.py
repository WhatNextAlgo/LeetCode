def diagonalSum(mat):
    n = len(mat)
    mid = n//2
    print(mid)
    total = sum([mat[x][x] + mat[x][n-1-x] for x in range(n)])
    if n % 2 != 0:
        total = total - mat[mid][mid]

    return total
    

        



print(diagonalSum( mat = [[5]]))