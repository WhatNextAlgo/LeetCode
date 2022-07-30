def subsetXORSum(nums):
    xor_sum = 0
    for i in nums:
        xor_sum |= i
    return xor_sum * 2 ** (len(nums)-1)




print(subsetXORSum(nums = [5,1,6]))
