def sortArrayByParityII1(nums):
    e = []
    o = []
    for x in nums:
        if x % 2 == 0:
            e.append(x)
        else:
            o.append(x)
    res = []
    for x , y in zip(e,o):
        res.append(x)
        res.append(y)
    
    return res

def sortArrayByParityII(nums):
    length =len(nums)
    even = 0
    odd = 1
    while even < length and odd < length:
        while even < length and nums[even] % 2 == 0:
            even += 2
        while  odd < length and nums[odd] % 2 != 0:
            odd +=2
        if even < length and odd < length:
            nums[odd],nums[even]  = nums[even],nums[odd]
        
        even += 2
        odd += 2
    return nums
print(sortArrayByParityII(nums = [4,2,5,7]))
