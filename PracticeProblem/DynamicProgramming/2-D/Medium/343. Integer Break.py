class Solution:
    #recursive dfs
    def integerBreak(self, n: int) -> int:
        
        def dfs(num):
            if num == 1:
                return 1
            res = 0 if num == n else num

            for l in range(1,num):
                val = dfs(l) * dfs(num -l)
                res = max(res,val)
            return res

        return dfs(n)
    # TOP -DOWN Memoization
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        def dfs(num):
            if num in dp:
                return dp[num]

            dp[num] = 0 if num == n else num

            for l in range(1,num):
                val = dfs(l) * dfs(num -l)
                dp[num] = max(dp[num] ,val)
            return dp[num] 

        return dfs(n)
    #DP
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        
        for num in range(2,n + 1):
            dp[num] = 0 if num == n else num
            for  i in range(1,num):
                val = dp[i] * dp[num - i]
                dp[num] = max(dp[num],val)

        return dp[n]

        


s = Solution()
print(s.integerBreak(n = 5))