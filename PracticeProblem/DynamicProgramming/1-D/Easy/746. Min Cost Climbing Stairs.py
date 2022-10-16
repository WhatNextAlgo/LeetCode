from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0) #To make math work out
        # right to left
        for i in range(len(cost)-3,-1,-1):
            cost[i] = min(cost[i + 1],cost[i + 2]) + cost[i]
        # we take the minimum of 0 and 1 index.
        return min(cost[0],cost[1]) 


s = Solution()
print(s.minCostClimbingStairs(cost = [10,15,20]))
print(s.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))
