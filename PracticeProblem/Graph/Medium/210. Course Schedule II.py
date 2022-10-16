from operator import truediv
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # map each course to prereq list
        preMap = { src: [] for src in range(numCourses)}
        for crs , pre in prerequisites:
            preMap[crs].append(pre)
        
        # a course  has 3 possible states:
        # visited -> crs has been added to output
        # visiting -> crs not added to output , but added to cycle
        # unvisited -> crs not been added to output and cycle

        cycle = set() 
        visited = set() # all cources along the cur DFS path
        output = []
        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False

            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):return []

        return output



s = Solution()
print(s.findOrder(numCourses = 2, prerequisites = [[1,0]]))
print(s.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
print(s.findOrder(numCourses = 6, prerequisites = [[1,0],[2,0],[3,1],[3,2],[5,0],[4,0]]))
print(s.findOrder(numCourses = 6, prerequisites = [[1,0],[2,0],[3,1],[3,2],[0,2],[5,0],[4,0]]))

