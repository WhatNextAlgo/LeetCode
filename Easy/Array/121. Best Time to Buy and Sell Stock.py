from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = prices[0]
        max_profit = 0
        for x in range(1,len(prices)):
            if prices[x] < max_val:
                max_val = prices[x]
            else:
                if max_profit < (prices[x] - max_val):
                    max_profit = (prices[x] - max_val)

        return max_profit


s = Solution()
print(s.maxProfit(prices = [3,3]))
