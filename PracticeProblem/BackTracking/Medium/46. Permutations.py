from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        #base case  
        if len(nums) == 1:
            return [nums[:]] # make copy of it

        for i in range(len(nums)):
            n = nums.pop(0) # pop the first value
            perms = self.permute(nums) # recursive call for next permutation
            print(perms,"--",n)
            for perm in perms:
                perm.append(n) # append the remove value at the end
            result.extend(perms) 
            nums.append(n) # return to original value
        return result

s = Solution()
print(s.permute(nums=[1,2,3]))
