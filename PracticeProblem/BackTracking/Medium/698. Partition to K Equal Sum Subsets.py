from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums)/k # calculat  the target value
        used = [False] * len(nums) # for track of value which one we are used

        def backtrack(i,k,subsetSum):
            if k == 0 :
                return True
            # found one of the subset then we have to start from the beginning
            # we can filter out which one are already used 
            if subsetSum == target: 
                return backtrack(0,k - 1,0)

            for j in range(i,len(nums)):
                if  used[j] or subsetSum + nums[j] > target:
                    continue

                used[j] = True
                if backtrack(j + 1, k,subsetSum + nums[j]):
                    return True
                used[j] = False

            return False

        return backtrack(0,k,0)


s = Solution()
print(s.canPartitionKSubsets(nums = [1,2,3,4], k = 3))