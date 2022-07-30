def sumOfUnique(nums):
    d= {}
    total = 0
    for x in nums:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    for x in d:
        if d[x] ==1:
            total += x

    return total


print(sumOfUnique(nums = [1,2,3,4,5]))