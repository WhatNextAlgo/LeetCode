import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for src , dest, w in times:
            edges[src].append((dest,w))

        minHeap = [(0,k)]
        visit = set()
        t = 0
        while minHeap:
            w1 , n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t,w1)
            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w2 + w1,n2))
        return t if len(visit) == n else -1




s = Solution()
print(s.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(s.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))