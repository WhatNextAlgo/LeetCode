def sortArrayByParity(nums):
    even,odd = [],[]
    for x in nums:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    return even + odd

def sortArrayByParity1(nums):
    lst = []
    e = 0
    for x in range(len(nums)):
        if nums[x] % 2 == 0:
            lst.insert(e,nums[x])
            e +=1
        else:
            lst.append(nums[x])

    return lst


print(sortArrayByParity1(nums = [3,1,2,4]))