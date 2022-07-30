from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def minCost(n,cost):
            dp = [None] * n
            if n == 1:
             return cost[0]

            dp[0] = cost[0]
            dp[1] = cost[1]
            for i in range(2, n):
                 dp[i] = min(dp[i - 1],
                            dp[i - 2]) + cost[i]

            print(dp)
            return min(dp[n - 2], dp[n - 1])


        n = len(cost)
       
        return minCost(n,cost)

        


s = Solution()
print(s.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))