class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            print(n)
            result += n & 1
            n = n >> 1
        # while n != 0:
        #     n &= n & 1
        #     result += 1
        return result

s= Solution()
print(s.hammingWeight(n = 11111111111111111111111111111101))
