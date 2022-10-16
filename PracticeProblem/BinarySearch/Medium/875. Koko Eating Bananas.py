import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # left pointer has to 1 cos aleast we need to eat
        # right pointer has to max value of piles so that we can eat each piles exactly in one hours

        l, r = 1, max(piles)

        res = r
        while l <=r :
            k = l + ((r - l)//2)
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h: # compute hours is less then given hours
                res = min(res,k) # we found so far best possible ans
                r = k - 1
            else:
                l = k + 1
        return res

            

s = Solution()
print(s.minEatingSpeed(piles = [3,6,7,11], h = 8))