class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_digit(n):
            total = 0
            while n > 0:
                val = (n % 10)
                total += (val * val)
                n = n//10
            return total
        not_happy=[2,3,4,5,6,8,9]
        while n != 1:
            if n in  not_happy:
                return False
            n = sum_of_digit(n)
        return True


s = Solution()
print(s.isHappy(n = 2))