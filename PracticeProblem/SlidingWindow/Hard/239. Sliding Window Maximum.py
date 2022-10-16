from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if k == 1 then window size is one therefore each an every value is maximum
        if k == 1:
            return nums 
        res = [] # store the output 
        q = deque() # monitonically Decreasing Queue
        l = r = 0  # left and right pointer
        while r < len(nums):

            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            #remove the left val for deque
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k: # edge case  where window size atleast size k
                res.append(nums[q[0]]) # append the first poisiton of queue
                l += 1 # increament the left pointer
            r += 1 # increament the right pointer
        return res


s = Solution()
print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
