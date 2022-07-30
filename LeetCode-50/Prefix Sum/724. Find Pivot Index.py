from typing import List
def pivotIndex(nums: List[int]) -> int:
    total = sum(nums)
    leftmost = 0
    for x in range(0,len(nums)):
        if leftmost == (total - leftmost -nums[x]):
            return x
        else:
            leftmost += nums[x]
    return -1
    

print(pivotIndex([-1,-1,-1,-1,-1,0]))
