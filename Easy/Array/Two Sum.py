def twoSum(nums, target):
    l = len(nums)
    for x in range(l-1):
        for y in range(x + 1, l):
            if nums[x] + nums[y] == target:
                return [x,y]
            
    return []
        

print(twoSum(nums = [3,2,3], target = 6))