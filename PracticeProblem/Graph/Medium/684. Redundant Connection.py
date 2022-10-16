from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = parent[n]
            while p != parent[n]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]


s = Solution()
print(s.findRedundantConnection(edges = [[1,2],[1,3],[2,3]]))
print(s.findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]))