def buildArray(nums):
    return [nums[nums[x]] for x in range(len(nums))]

print(buildArray([5,0,1,2,3,4]))
    