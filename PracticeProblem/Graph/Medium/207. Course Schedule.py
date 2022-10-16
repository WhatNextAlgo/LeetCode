from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        preMap = { src: [] for src in range(numCourses)}
        for crs , pre in prerequisites:
            preMap[crs].append(pre)
        
        visitedSet = set() # all cources along the cur DFS path

        def dfs(crs):
            if crs in visitedSet:
                return False

            if preMap[crs] == []:
                return True

            visitedSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitedSet.remove(crs) # no longer to visit again
            preMap[crs] = [] # we are able to complete crs
            return True

        for crs in range(numCourses):
            if not dfs(crs):return False

        return True



s = Solution()
print(s.canFinish(numCourses = 2, prerequisites = [[1,0]]))
print(s.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))