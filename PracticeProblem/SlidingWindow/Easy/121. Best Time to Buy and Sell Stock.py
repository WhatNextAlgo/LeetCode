from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 # maximum profit
        l = 0 # left pointer
        for r in range(1,len(prices)): # r is right pointer
            if prices[r] < prices[l]:
                l = r # update the pointer when we find the lowest price to buy
            
            res = max(res, prices[r] - prices[l]) 
        
        return res

s = Solution()
print(s.maxProfit(prices = [7,1,5,3,6,4]))
print(s.maxProfit(prices = [7,6,4,3,1]))
