class Solution:
    def fib(self, n: int) -> int:
        r=  [-1] * (n+2)
        return self.climbing_helper(n + 1,r)

    def climbing_helper(self,n,r):

        if r[n] >= 0:
            return r[n]

        
        if n <= 1:
            q = n

        else:
            q = self.climbing_helper(n - 1, r) + self.climbing_helper(n - 2, r)

        r[n] = q
        return q


s = Solution()
print(s.fib(-1))


        
        