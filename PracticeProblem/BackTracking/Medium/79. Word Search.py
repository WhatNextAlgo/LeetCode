from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board),len(board[0])
        visit = set()

        def dfs(r,c,i):
            if i == len(word):
                return True

            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r,c) in visit or word[i] != board[r][c]):
                return False

            visit.add((r,c))
            # if any of the cell we found match then return True  
            res =  (dfs(r + 1,c,i + 1) or 
                    dfs(r - 1,c,i + 1) or
                    dfs(r,c + 1,i + 1) or
                    dfs(r,c - 1,i + 1))
            visit.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):return True

        return False




s = Solution()
print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))