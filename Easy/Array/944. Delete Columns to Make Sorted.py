def minDeletionSize(strs):
    matrix = [list(x) for x in strs]
    row_len = len(matrix[0])
    col_len = len(matrix)

    delete_count = 0
    for x in range(row_len):
        for y in range(col_len-1):
            if ord(matrix[y][x]) > ord(matrix[y+1][x]):
                delete_count += 1
                break
    return delete_count

print(minDeletionSize(strs = ["zyx","wvu","tsr"]))