from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1 # goal point to last position
        for i in range(len(nums)-1,-1,-1):
            # from that i position + value in it.can we reach to goal post or not?
            if i + nums[i] >= goal: 
                goal = i
        return True if goal == 0 else False

s = Solution()
print(s.canJump(nums = [2,3,1,1,4]))
print(s.canJump(nums = [2,3,1,1,4]))