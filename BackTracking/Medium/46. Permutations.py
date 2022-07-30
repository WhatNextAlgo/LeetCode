from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        result = []
        
        for _ in range(len(nums)):
            n = nums.pop(0)

            prems = self.permute(nums)

            for prem in prems:
                prem.append(n)
            result.extend(prems)
            nums.append(n)

        return result

s = Solution()
print(s.permute(nums = [1,2,3]))
