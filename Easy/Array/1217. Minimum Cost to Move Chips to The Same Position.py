def minCostToMoveChips(position):
    even = odd = 0
    for x in position:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1

    return min(even,odd)



print(minCostToMoveChips(position = [1,2,3]))