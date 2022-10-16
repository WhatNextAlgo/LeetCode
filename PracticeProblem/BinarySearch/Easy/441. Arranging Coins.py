class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        res = 0
        while l <= r:
            mid = l + ((r - l)//2)
            coins =  (mid + 1) * (mid/2)
            if coins > n:
                r = mid - 1
            else:
                res = max(res,mid)
                l = mid + 1
        return res


s = Solution()
print(s.arrangeCoins(n = 6))