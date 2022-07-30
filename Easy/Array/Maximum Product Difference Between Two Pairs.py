def maxProductDifference(nums):
    nums.sort()
    return (nums[-1] * nums[-2]) - (nums[0] * nums[1])


print(maxProductDifference(nums = [4,2,5,9,7,4,8]))