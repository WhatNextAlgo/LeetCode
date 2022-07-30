def smallestEqual(nums):
    for x in range(len(nums)):
        if x % 10 == nums[x]:
            return x
    else:
        return -1


print(smallestEqual(nums = [1,2,3,4,5,6,7,8,9,0]))