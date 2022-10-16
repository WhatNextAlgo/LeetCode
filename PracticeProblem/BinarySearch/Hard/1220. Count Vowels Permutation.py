class Solution:
    def countVowelPermutation(self, n: int) -> int:
        #dp[j][c] = nums of strs of len=j;
        #where last char is c:
        dp = [[],[1,1,1,1,1]]

        a,e,i,o,u = 0,1,2,3,4
        mod = 10**9 + 7

        for j in range(2,n + 1):
            dp.append([0,0,0,0,0])

            dp[j][a] = (dp[j-1][e] + dp[j-1][i] + dp[j-1][u]) %mod # ending with a
            dp[j][e] = (dp[j-1][a] + dp[j-1][i]) %mod # ending e
            dp[j][i] = (dp[j-1][e] + dp[j-1][o]) %mod # ending i
            dp[j][o] = (dp[j-1][i]) %mod # ending o
            dp[j][u] = (dp[j-1][i] + dp[j-1][o]) %mod #ending u

        return sum(dp[n]) %mod


    def countVowelPermutation1(self, n: int) -> int:
        # Initialize all vowels counts to 1
		# This is n==1 case
        a, e, i, o, u = 1, 1, 1, 1, 1

        # Iterate from 2 to n
        for _ in range(2, n + 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o

        # Return the sum of all counts of all vowels
        return (a + e + i + o + u) % 1000000007

s = Solution()
print(s.countVowelPermutation(n = 5))