from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS = len(board),len(board[0])

        def capture(r,c):
            if (r < 0 or r >= ROWS or c <0 or c >= COLS or
                board[r][c] != 'O'):
                return 
            
            board[r][c] = 'T'
            capture(r + 1,c)
            capture(r - 1,c)
            capture(r ,c + 1)
            capture(r,c - 1)
        
        # 1. Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0,ROWS-1] or c in [0,COLS-1]):
                    capture(r,c)

        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncapture unsurronded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

        print(board)



s = Solution()
print(s.solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
