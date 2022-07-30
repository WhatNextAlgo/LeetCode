class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def sub_prod_sum_helper(n):
            prod = 1
            sum = 0
            while n >0:
                val = n % 10
                n = n//10
                prod *= val
                sum += val
            
            return prod- sum
        return sub_prod_sum_helper(n)



s = Solution()
print(s.subtractProductAndSum(n=234))