
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1,n + 1):
            for s in range(1,target + 1): # 1 to target
                square = s * s
                if target -square < 0:
                    break
                dp[target] = min(dp[target],1 + dp[target - square])
        print(dp)
        return dp[n]

s = Solution()
print(s.numSquares(n = 12))
