from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        up = down = 1
        for x  in range(1,len(nums)):
            if nums[x] > nums[x-1]:
                up = down + 1
            elif nums[x] < nums[x-1]:
                down = up + 1
        

        return max(down,up)


            




s= Solution()
print(s.wiggleMaxLength(nums = [1,2,3,4,5,6,7,8,9]))
        