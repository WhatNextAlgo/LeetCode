class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set() # r + c
        negDiag = set() # r - c
        res = 0

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return 

            for c in range(n):
                if c in col or (r + c) in posDiag or (r -c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return res

s = Solution()
print(s.totalNQueens(n = 4))