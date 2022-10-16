from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums)-1
        while l <= r :
            m = l + ((r - l)//2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return l


s = Solution()
print(s.searchInsert(nums = [1,3,5,6], target = 5))
print(s.searchInsert(nums = [1,3,5,6], target = 2))
print(s.searchInsert(nums = [1,3,5,6], target = 7))
