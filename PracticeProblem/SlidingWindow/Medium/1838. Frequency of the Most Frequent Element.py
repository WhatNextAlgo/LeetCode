from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort() # sort the list in asc order
        l= 0 # left pointer
        res = 0 
        total = 0
        for r in range(len(nums)):
            total += nums[r] # sum of sliding window
            #rightmost elem * windowLen > sum of sliding window + k then 
            # subtract the left most val and increment left pointer
            if nums[r] * (r - l + 1) > total + k: 
                total -= nums[l]
                l += 1
            res = max(res, (r - l + 1)) # update the result

        return res


s = Solution()
print(s.maxFrequency(nums = [1,2,4], k = 5))