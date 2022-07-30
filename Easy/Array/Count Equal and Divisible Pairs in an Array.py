def countPairs(nums, k):
    n = len(nums)
    count = 0
    for x in range(n):
        for y in range(x + 1, n):
            if nums[x] == nums[y] and (x * y) % k == 0:
                count +=1

    return count 


print(countPairs(nums = [1,2,3,4], k = 1))