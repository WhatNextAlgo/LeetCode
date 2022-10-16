from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,cur,total):
            if total == target:
                res.append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return

            # decision to include candidates
            cur.append(candidates[i])
            dfs(i,cur,total + candidates[i])

            # decision to include candidates
            cur.pop()
            dfs(i + 1,cur,total)

        dfs(0,[],0)
        return res

s = Solution()
print(s.combinationSum( candidates = [2,3,6,7], target = 7))