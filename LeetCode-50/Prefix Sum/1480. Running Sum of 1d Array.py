from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if nums != []:
            lst = [0] * len(nums)

            lst[0] = nums[0]
            for x in range(1,len(nums)):
                lst[x] = nums[x] + lst[x-1]

            return lst
        return []