from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) -1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = l + ((r - l)//2)
            res = min(res,nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return res 
            


s = Solution()
print(s.findMin(nums = [3,4,5,1,2]))
print(s.findMin(nums = [4,5,6,7,0,1,2]))