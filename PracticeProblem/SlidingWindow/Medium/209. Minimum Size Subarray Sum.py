from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , total = 0,0
        res = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res,r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res


s = Solution()
print(s.minSubArrayLen( target = 11, nums = [1,1,1,1,1,1,1,1]))