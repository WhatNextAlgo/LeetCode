from collections import deque
from typing import List


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        ROWS,COLS = len(rooms),len(rooms[0])
        visit = set()
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        print(q)

        dist = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            for _ in range(len(q)):
                r , c = q.popleft()
                rooms[r][c] = dist
                for dr , dc in directions:
                    neiR,neiC = r + dr, c + dc
                    if (neiR < 0 or neiC < 0 or neiR >= ROWS 
                        or neiC >= COLS or (neiR,neiC) in visit or rooms[neiR][neiC] == -1):
                        continue
                    visit.add((neiR,neiC))
                    q.append([neiR,neiC])

            dist += 1
        print(rooms)

        





s = Solution()
s.walls_and_gates(rooms=[
    [2322424424,-1,0,2322424424],
    [2322424424,2322424424,2322424424,-1],
    [2322424424,-1,2322424424,-1],
    [0,-1,2322424424,2322424424]
    ])