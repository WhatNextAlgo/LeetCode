
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #map each course to prereq list
        preMap = {src: [] for src in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        #visitedSet = all courses along the curr DFS path
        visitedSet = set()

        def dfs(crs):
            if crs in visitedSet:
                return False
            
            if preMap[crs] == []:
                return True

            visitedSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):return False
            visitedSet.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):return False
        return True
         


