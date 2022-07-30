def maxProduct(nums):
    nums.sort()
    return (nums[-1] -1) * (nums[-2]-1)

print(maxProduct(nums = [3,7]))