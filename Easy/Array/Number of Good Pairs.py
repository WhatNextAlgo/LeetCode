def numIdenticalPairs(nums):
    length = len(nums)
    count = 0
    for x in range(length):
        for y in range(x + 1,length):
            if nums[x] == nums[y]:
                count += 1
    return  count


print(numIdenticalPairs([1,2,3]))