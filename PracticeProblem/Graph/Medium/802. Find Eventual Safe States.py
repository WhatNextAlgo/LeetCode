from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False # initally we mark as not a safe not
            for nei in graph[i]:
                if not dfs(nei):
                    return safe[nei]

            safe[i] = True
            return safe[i]


        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res

s = Solution()
print(s.eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]]))
print(s.eventualSafeNodes(graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]))
