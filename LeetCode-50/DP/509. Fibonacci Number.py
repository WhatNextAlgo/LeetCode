class Solution:
    def fib(self, n: int) -> int:
        r=  [-1] * (n+2)
        return self.fibonacci_helper(n + 1,r)

    def fibonacci_helper(self,n,r):

        if r[n] >= 0:
            return r[n]

        
        if n <= 1:
            q = n

        else:
            q = self.fibonacci_helper(n - 1, r) + self.fibonacci_helper(n - 2, r)

        r[n] = q
        return q


s = Solution()
print(s.fib(-1))


        
        