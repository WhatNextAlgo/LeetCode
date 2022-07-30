from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def intToPro(square):
            r = (square -1 )//length
            c = (square - 1) % length
            if r % 2 :
                c = length - 1 - c
            return [r,c]
        
        q = deque()
        q.append([1,0])
        visit = set()
        while q :
            square,moves = q.popleft()
            for i in  range(1, 7):
                nextSquare = square + i
                r,c = intToPro(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                
                if nextSquare == length * length:
                    return moves + 1
                
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare,moves + 1])
        return -1

s = Solution()
print(s.snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))