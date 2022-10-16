from typing import List

#bellman ford Algorithms
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        # loop for k + 1 time
        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue

                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        
        return -1 if prices[dst] == float('inf') else prices[dst]



s = Solution()
print(s.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
 src = 0, dst = 3, k = 1))