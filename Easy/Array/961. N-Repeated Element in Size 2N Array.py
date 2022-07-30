def repeatedNTimes(nums):
    lst = []
    for x in nums:
        if x not in lst:
            lst.append(x)
        else:
            return x


    
print(repeatedNTimes(nums = [5,1,5,2,5,3,5,4]))