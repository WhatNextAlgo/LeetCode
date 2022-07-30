from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_index = -1
        min_dist = float('inf')
        for  ind, i  in enumerate(points):
            if (x == i[0] or y == i[1]) and (min_dist > (abs(x -  i[0]) + abs(y - i[1]))):
                min_dist = (abs(x -  i[0]) + abs(y - i[1]))
                min_index = ind
                print(min_index)
            
        return min_index

        
    


s = Solution()
print(s.nearestValidPoint( x = 1, y = 1, points = [[1,1],[1,1]]))

if (0 > 0):
    print(True)

