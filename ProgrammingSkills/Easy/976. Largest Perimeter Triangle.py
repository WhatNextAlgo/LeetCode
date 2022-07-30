from typing import List


class Solution:
    def largestPerimeter1(self, nums: List[int]) -> int:
        mx = 0
        n = len(nums)
        for x in range(n-2):
            for y in range(x + 1,n-1):
                for z in range(y + 1,n):
                    a,b,c =  nums[x],nums[y],nums[z]
                    if (a < b + c) and (b < a+ c) and (c < a + b):
                        mx = max(mx,a + b + c)
        return mx

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        mx = 0
        n = len(nums)
        for x in range(0,n-2):
                    a,b,c =  nums[x],nums[x + 1],nums[x + 2]
                    if (a < b + c) and (b < a+ c) and (c < a + b):
                        mx = max(mx,a + b + c)
        return mx


s = Solution()
print(s.largestPerimeter(nums = [3,2,3,4]))