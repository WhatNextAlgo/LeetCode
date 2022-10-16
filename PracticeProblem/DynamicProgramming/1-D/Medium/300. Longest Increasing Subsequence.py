from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)


    def lengthOfLIS1(self, nums: List[int]) -> int:
        arr = [nums.pop(0)]                 
 
        for n in nums:                      
            
            if n > arr[-1]:                 
                arr.append(n)

            else:                            
                arr[bisect_left(arr, n)] = n 

        return len(arr) 
s = Solution()
print(s.lengthOfLIS( nums = [10,9,2,5,3,7,101,18]))