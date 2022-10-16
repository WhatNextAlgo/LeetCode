from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l , r = 0,0 # determine the level window
        while r < len(nums) -1:
            farthest = 0
            for i in range(l,r + 1):
                farthest = max(farthest,i + nums[i])
            
            l = r + 1
            r = farthest
            res += 1
        return res

s = Solution()
print(s.jump(nums = [2,3,1,1,4]))
        
