from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in unique:
                length = 1
                while (n + length) in unique:
                        length += 1
                longest = max(length, longest)
        return longest  


s= Solution()
print(s.longestConsecutive(nums = [0,0]))