from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for x in nums:
            if x in d:
                return True
            d[x] = 1
        return False