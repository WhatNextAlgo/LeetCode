from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        prem = []
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)

        def dfs():
            if len(prem) == len(nums):
                res.append(prem[:])
                return
            for n in count:
                if  count[n] >0:
                    prem.append(n)
                    count[n] -= 1
                    dfs()
                    count[n]+= 1
                    prem.pop()
        dfs()
        return res

s = Solution()
print(s.permuteUnique(nums=[1,1,2]))
        