from typing import List


def singleNumber1(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    for x in nums:
        if nums.count(x) == 1:
            return x

def singleNumber(nums: List[int]) -> int:
    ans = 0
    for x in nums:
        ans ^= x
    return ans

print(singleNumber(nums = [4,1,2,1,2]))