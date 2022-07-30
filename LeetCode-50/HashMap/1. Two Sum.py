from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, n in enumerate(nums):
            if (target - n) in d:
                return [d[target-n], index]
            else:
                d[n] = index
    
                

s = Solution()
print(s.twoSum(nums = [0,4,3,0], target = 0))
print(s.twoSum(nums = [3,3], target = 6))
        
