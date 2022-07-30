import math


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        strLenHalf = math.pow(2,n-2)
        isZero:bool = True

        while n > 1:
            if k > strLenHalf:
                isZero = not isZero
                k -= strLenHalf

            n -= 1
            strLenHalf /= 2
        return 0 if isZero else 1

    



s = Solution()
print(s.kthGrammar(n = 2, k = 2 ))
