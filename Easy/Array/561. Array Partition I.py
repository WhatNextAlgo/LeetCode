def arrayPairSum(nums):
    result = 0
    nums.sort()
    for x in range(0,len(nums)-1,2):
        print(x)
        result += min(nums[x],nums[x+1])
    return result

print(arrayPairSum(nums = [6,2,6,5,1,2]))