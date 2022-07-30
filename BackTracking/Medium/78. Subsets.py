from typing import List


class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        lst = []
        N = len(nums)
        for x  in range(1<<N):
            data = []
            for y in range(N):
                if(x & (1 << y)):
                    data.append(nums[y])
            lst.append(data)
        return lst

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res


s = Solution()
print(s.subsets(nums = [1,2,3]))