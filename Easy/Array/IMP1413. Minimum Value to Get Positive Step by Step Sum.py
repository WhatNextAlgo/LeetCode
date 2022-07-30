from typing import List


def minStartValue(nums: List[int]) -> int:
    min_sum, ans =0,0
    for x in nums:
        min_sum = min_sum + x
        ans = min(ans,min_sum)
    return -ans + 1


print(minStartValue(nums = [-3,2,-3,4,2]))