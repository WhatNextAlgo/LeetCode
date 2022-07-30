def minSubsequence(nums):
    minSubArray = []
    nums.sort()
    total =  sum(nums)
    temp = 0
    for y in range(len(nums)-1,-1,-1):
        if (temp > total/2):
            break
        minSubArray.append(nums[y])
        temp += nums[y]

    return minSubArray






print(minSubsequence(nums = [4,4,7,6,7]))