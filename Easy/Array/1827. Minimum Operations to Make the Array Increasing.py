def minOperations(nums):
    count = 0
    lst = [nums[0]]
    for x in range(1,len(nums)):
        if nums[x] <= lst[x-1]:
            d = abs(nums[x] - lst[x-1]) + 1
            count += d
            lst.append(d + nums[x])
        else:
            lst.append(nums[x])
    return count


print(minOperations( nums = [1,5,2,4,1]))