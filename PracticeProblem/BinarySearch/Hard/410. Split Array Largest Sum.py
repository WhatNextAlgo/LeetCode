from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        def canSplit(largest): # can split in m group
            subarry = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarry += 1
                    # we know after adding n we exceed the largest value 
                    # so we need to start from n to next subarray
                    curSum = n 
            return subarry + 1 <= m
        l , r = max(nums), sum(nums) # create a binary seacrh range
        res = r # so far best solution
        while l <= r:
            mid = l + ((r - l)//2)
            print(mid)
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                print("else")
                l = mid + 1

        return res

    def splitArray(self, nums: List[int], m: int) -> int:
        dp = {}
        def dfs(i,m):
            if m == 1:
                return sum(nums[i:])

            if (i,m) in dp:
                return dp[(i,m)]

            res, curSum = float("inf"),0
            for j in range(i, len(nums)-m + 1):
                curSum += nums[j]
                maxSum = max(curSum,dfs(j + 1, m - 1))
                res = min(res,maxSum)
                if curSum >  res:
                    break
            dp[(i,m)] = res
            return res

        return dfs(0,m)




s = Solution()
print(s.splitArray(nums = [7,2,5,10,8], m = 2))


