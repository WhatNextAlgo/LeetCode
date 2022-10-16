# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    if num == 6:
        return 0
    elif num > 6:
        return -1
    else:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <=r:
            mid = l + ((r - l)//2)
            res = guess(mid)
            if res > 0:
                l = mid + 1
            elif res < 0:
                r = mid - 1
            else:
                return mid

s = Solution()
print(s.guessNumber(n = 10))
    