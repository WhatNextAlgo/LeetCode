from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums,target,True)
        right = self.binarySearch(nums,target,False)
        return [left,right]
        

    
    def binarySearch(self,nums:List[int],target:int,leftBias:bool) -> int:
        l, r = 0, len(nums) -1
        i = -1

        while l <= r:
            m = l + ((r - l)//2)
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else: 
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i



s = Solution()
print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))
print(s.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(s.searchRange(nums=[],target= 0))