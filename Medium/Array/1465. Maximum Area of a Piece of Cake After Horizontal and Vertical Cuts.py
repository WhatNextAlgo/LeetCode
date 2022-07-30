from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # adding lower and upper limit to horizontalCuts
        horizontalCuts.append(0)                            
        horizontalCuts.append(h)
        
        # adding lower and upper limit to verticalCuts
        verticalCuts.append(0)
        verticalCuts.append(w)
        
        verticalCuts.sort()
        horizontalCuts.sort()

        h_max = self.find_max_diff(verticalCuts)            
        v_max = self.find_max_diff(horizontalCuts)         
        
        def find_max_diff(arr):
            max_diff = 0
            for i in range(1,len(arr)):
                max_diff = max(max_diff, arr[i]-arr[i-1])
            return max_diff


        return (h_max*v_max)%(10**9+7) 


s = Solution()
print(s.maxArea(h = 1000000000, w = 1000000000, horizontalCuts = [2], verticalCuts = [2]))

