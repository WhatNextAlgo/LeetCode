from typing import List
import math


class Solution:
    class Solution:
        def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
            dp = [[[math.inf for k in range(target + 1)] for j in range(n + 1)] for i in range(m + 1)]
            for j in range(n + 1):
                dp[0][j][0] = 0
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    # The current house has already been painted, no need to consider other colors
                    if houses[i - 1] and houses[i - 1] != j:
                        continue
                    for k in range(1, target + 1):
                        ls = [dp[i - 1][jj][k - 1] for jj in range(1, n + 1) if jj != j] + [dp[i - 1][j][k]]
                        dp[i][j][k] = min(ls)
                        if houses[i - 1] == 0: # Only add paint cost if it hasn't been painted before
                            dp[i][j][k] += cost[i - 1][j - 1]
            ans = min([dp[m][j][target] for j in range(1, n + 1)])
            if ans == math.inf:
                return -1
            return ans


s = Solution()
print(s.minCost(houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3))