from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i,cur):
            if len(cur) == k:
                res.append(cur[:])
                return

            for j in range(i,n + 1):
                cur.append(j)
                backtrack(j + 1,cur)
                cur.pop()

        backtrack(1,[])
        return res


s = Solution()
print(s.combine(n = 4, k = 2))