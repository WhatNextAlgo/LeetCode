class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {} # (i,j) # index of s and t

        def dfs(i,j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if s[i] == t[j]:
                dp[(i,j)] = dfs(i + 1, j + 1) + dfs(i + 1,j)
            else:
                dp[(i,j)] = dfs(i + 1,j)

            return dp[(i,j)]
        
        return dfs(0,0)

s = Solution()
print(s.numDistinct(s = "rabbbit", t = "rabbit"))