def runningSum(nums):
    if nums != []:
        lst = [0] * len(nums)
        
        lst[0] = nums[0]
        for x in range(1,len(nums)):
            lst[x] = nums[x] + lst[x-1]

        return lst
    else:
        return []

print(runningSum([3,1,2,10,1]))
