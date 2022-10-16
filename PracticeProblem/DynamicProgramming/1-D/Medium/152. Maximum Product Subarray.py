from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # 0 -> [-1]
        curMin, curMax = 1,1
        for n in nums:
            if n == 0:
                curMin,curMin = 1,1
            temp = n * curMax
            curMax = max(n * curMax,n * curMin,n)
            curMin = min(temp,n * curMin,n)
            res = max(curMax,res)
        return res


s = Solution()
print(s.maxProduct(nums = [2,3,-2,4]))
print(s.maxProduct(nums = [-2,0,-1]))
