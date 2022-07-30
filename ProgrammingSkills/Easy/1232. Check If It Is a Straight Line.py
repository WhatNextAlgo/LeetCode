from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n=1
        l=len(coordinates)
        #Slope of line formed by two points (y2, y1), (x2, x1)
        x0,y0=coordinates[0][0],coordinates[0][1]
        x1,y1=coordinates[1][0],coordinates[1][1]

        dx = x1 - x0
        dy = y1 - y0

        while n<l:
    
            if (coordinates[n][0]-x0)*(dy)!=(coordinates[n][1]-y0)*(dx):
                return False
            n+=1
        return True


s = Solution()
print(s.checkStraightLine(coordinates = [[0,0],[0,1],[0,-1]]))

            
                