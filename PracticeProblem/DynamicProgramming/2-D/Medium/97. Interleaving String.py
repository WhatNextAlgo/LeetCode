class Solution:
    #Memoization
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {} # (i,j) -> of (s1 index,s2 index)

        def dfs(i,j):
            if i == len(s1) and j == len(s2):
                return True
            
            if (i,j) in dp:
                return dp[(i,j)]

            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1,j):
                return True
            
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i,j + 1):
                return True
            dp[(i,j)] = False
            return False

        return dfs(0,0)

    #Classic Dp
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if  i < len(s1) and s1[i] == s3[i + j] and dp[i+1][j]:
                    dp[i][j] = True
                
                if  j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        print(dp)
        return dp[0][0]
                
     
[[True, False, False, False, False, False],
[True, False, False, False, False, False],
[True, True, True, True, True, False],
[False, True, True, False, True, False],
[False, False, True, True, True, True],
[False, False, False, False, False, True]]





s = Solution()
print(s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))