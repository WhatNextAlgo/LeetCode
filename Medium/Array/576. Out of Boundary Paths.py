from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def dfs(startRow,startColumn,maxMove):
            if startRow == m or startColumn == n or startRow < 0 or startColumn < 0:
                return 1
            if maxMove == 0:
                return 0
            return (self.findPaths(m,n,maxMove-1,startRow-1,startColumn)
                + self.findPaths(m,n,maxMove-1,startRow+1,startColumn)
                + self.findPaths(m,n,maxMove-1,startRow,startColumn -1)
                + self.findPaths(m,n,maxMove-1,startRow,startColumn + 1))
        mod = 10**9 + 7
        return dfs(startRow,startColumn,maxMove) % mod
        


    def findPaths1(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dp(i,j,moves):
            if i < 0 or j < 0 or i >= m or j >= n: return 1
            if moves == 0:
                return 0

            ans  = 0
            for d in directions:
                ni =  i + d[0]
                nj =  j + d[1]
                ans += dp(ni,nj,moves-1)
            return ans

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        mod = 10**9 + 7
        return dp(startRow,startColumn,maxMove) % mod


s = Solution()
print(s.findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))
        