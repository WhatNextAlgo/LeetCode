from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i,subset):
            if i == len(nums):
                res.append(subset[:])
                return
            # ALL subset that include nums[i]
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()

            # All subset that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i+1,subset)

        backtrack(0,[])
        return res

s = Solution()
print(s.subsetsWithDup(nums = [1,2,2]))