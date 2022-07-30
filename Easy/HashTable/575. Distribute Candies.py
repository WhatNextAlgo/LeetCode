from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        d = {}
        for x in candyType:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        n = len(candyType)// 2
        return min(n,len(d))
        


s = Solution()
print(s.distributeCandies(candyType = [6,6,6,6]))