from typing import List


def findMin(nums: List[int]) -> int:
    n = len(nums)
    if n ==1:
        return nums[0]
    
    for x in range(n):
        if nums[x] <= nums[-1]:
            return nums[x]
    return -1
print(findMin(nums = [4,5,6,7,0,1,2]))
#print(findMin(nums = [11,13,15,17]))

