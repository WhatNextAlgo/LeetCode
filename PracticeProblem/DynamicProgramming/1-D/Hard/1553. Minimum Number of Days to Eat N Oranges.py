class Solution:
    def minDays(self, n: int) -> int:
        dp = {0:0,1:1}

        # n is no of oranges
        def dfs(n):
            if n in dp:
                return dp[n]

            one = 1 + (n % 2) + dfs(n//2) 
            two =  1 + (n % 3) + dfs(n // 3)
            dp[n] =min(one,two)
            return dp[n]

        return dfs(10)
s= Solution()
print(s.minDays(n = 10))