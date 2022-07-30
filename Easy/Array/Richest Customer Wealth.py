def maximumWealth(accounts):
    return max([sum(x) for x in accounts])

print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))