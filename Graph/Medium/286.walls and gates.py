from collections import deque
from typing import List


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        ROWS, COLS = len(rooms), len(rooms[0])
        print(ROWS)
        print(COLS)
        visit = set()
        q =[]

        for r in range(ROWS):
            for c in range(COLS):
                print(r,c)
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        def addRooms(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or rooms[r][c] == -1:
                return

            visit.add((r,c))
            q.append([r,c])

        
        dist = 0
        while q:
            for _ in range(len(q)):
                r,c = q.pop(0)
                rooms[r][c] = dist
                addRooms(r + 1,c)
                addRooms(r - 1,c)
                addRooms(r,c + 1)
                addRooms(r,c -1 )
            dist += 1
        print(rooms)

        





s = Solution()
s.walls_and_gates(rooms=[
    [2322424424,-1,0,2322424424],
    [2322424424,2322424424,2322424424,-1],
    [2322424424,-1,2322424424,-1],
    [0,-1,2322424424,2322424424]
    ])