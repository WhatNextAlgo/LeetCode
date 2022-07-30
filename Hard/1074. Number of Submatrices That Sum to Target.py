import collections
from typing import  List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1,n):
                matrix[i][j] += matrix[i][j-1]
        
        print(matrix)
        ans = 0
        #submatrix column division for each pair of columns
        for sc1 in range(n):
            for sc2 in range(sc1,n):
                d = collections.defaultdict(int)
                ## sum 0
                d[0] = 1
                #submatrix sum
                s = 0
                for i in range(m):
                    s += matrix[i][sc2]
                    #remove previous column sums
                    print(s)
                    if sc1:
                        s -= matrix[i][sc1-1]
                    print("s-target",d[s-target])
                    ans += d[s-target]
                    d[s] += 1
        return ans

s = Solution()
print(s.numSubmatrixSumTarget(matrix = [[1,-1],[-1,1]], target = 0))