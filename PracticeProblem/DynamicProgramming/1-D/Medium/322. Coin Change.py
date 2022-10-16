from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp =[amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1,amount + 1):
            for c in coins:
                if a - c >= 0:
                    # target = 7
                    # dp[7] = 1(no of coins) + dp[6]
                    # dp[4] = 1 + dp[3]
                    dp[a] = min(dp[a],1 + dp[a -c])

        return dp[amount] if dp[amount] != amount + 1 else -1


s = Solution()
print(s.coinChange(coins = [1,2,5], amount = 11))
print(s.coinChange(coins = [1,3,4,5], amount = 7))
