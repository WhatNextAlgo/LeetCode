from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index,total)
        
        def dfs(i,total):
            if i == len(nums):
                return 1 if total == target else 0

            if (i,total) in dp:
                return dp[(i,total)]

            dp[(i,total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1,total - nums[i])
            return dp[(i,total)]


        return dfs(0,0)


s = Solution()
print(s.findTargetSumWays(nums = [1,1,1,1,1], target = 3))