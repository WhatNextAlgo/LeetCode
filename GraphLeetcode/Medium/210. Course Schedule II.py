from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preReq[crs].append(pre)
        
        output = []
        visitSet, cycle = set(),set()

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visitSet:
                return True

            cycle.add(crs)
            for pre in preReq[crs]:
                if dfs(pre) == False:return False
            
            cycle.remove(crs)
            visitSet.add(crs)
            output.append(crs)
            return True
        for crs in range(numCourses):
            if dfs(crs) == False:return []
        
        return output

s = Solution()
print(s.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))