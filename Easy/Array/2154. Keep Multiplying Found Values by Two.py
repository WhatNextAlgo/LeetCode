def findFinalValue(nums, original):
    nums.sort()
    for x in nums:
        if original == x:
            original = original * 2
    return original


print(findFinalValue(nums = [8,19,4,2,15,3], original = 2))