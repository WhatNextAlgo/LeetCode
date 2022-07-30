from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_seen = max_seen_so_far = nums[0] 

        for i in range(1,len(nums)):
            if max_seen > 0:
                max_seen += nums[i]
            else:
                max_seen = nums[i]
            if max_seen > max_seen_so_far:
                max_seen_so_far = max_seen

        return max_seen_so_far


        



s =  Solution()
print(s.maxSubArray(nums = [5,4,-1,7,8]))

"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""