from typing import List


class Solution:
    # Recursive : Top DOWN Memoization
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        # i = index, even = True/False, total = current sum

        def dfs(i, even):
            if i == len(nums):
                return 0
            if (i , even) in dp:
                return dp[(i,even)]
            
            total = nums[i] if even else (-1 * nums[i])
            dp[(i,even)] = max(total + dfs(i + 1,not even), dfs(i + 1,even))
            return dp[(i,even)] 

        return dfs(0,True)

    def maxAlternatingSum(self, nums: List[int]) -> int:
        sumEven,sumOdd = 0,0

        for i in range(len(nums)-1,-1,-1):
            tmpEven = max(sumOdd + nums[i],sumEven)
            tmpOdd = max(sumEven - nums[i],sumOdd)
            sumEven,sumOdd = tmpEven,tmpOdd

        return sumEven

s = Solution()
print(s.maxAlternatingSum(nums = [4,2,5,3]))