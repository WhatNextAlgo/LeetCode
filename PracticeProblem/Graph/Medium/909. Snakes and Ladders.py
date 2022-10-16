from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        def intToPos(square):
            r = (square- 1) //length
            c = (square -1 ) % length
            if r % 2:
                c = length -1 - c
            return [ r,c]
        
        q = deque() # [ square/cell,moves]
        q.append([1,0])
        visit = set()
        while q:
            square, moves = q.popleft()
            for i in range(1,7):
                nextSqaure = square + i
                r,c = intToPos(nextSqaure)
                if board[r][c] != -1:
                    nextSqaure =board[r][c]
                if nextSqaure == length * length:
                    return moves + 1
                if nextSqaure not in visit:
                    visit.add(nextSqaure)
                    q.append([nextSqaure,moves + 1])
        return -1

s = Solution()
print(s.snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],
                                    [-1,-1,-1,-1,-1,-1],
                                    [-1,-1,-1,-1,-1,-1],
                                    [-1,35,-1,-1,13,-1],
                                    [-1,-1,-1,-1,-1,-1],
                                    [-1,15,-1,-1,-1,-1]]))