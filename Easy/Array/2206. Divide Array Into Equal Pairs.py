def divideArray(nums):
    length = len(nums)
    if length % 2 == 0 and length !=0:
        nums.sort()
        for x in range(0,length,2):
            if nums[x] != nums[x+1]:
                return False
        return True
    
    return False




print(divideArray(nums = []))