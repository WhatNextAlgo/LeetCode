from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if rows * cols != r * c:
            return mat

        one_dim = []
        for x in mat:
            one_dim += x
        result = []
    
        i = 0
        for x in range(r):
            temp = []
            for _ in range(c):
                temp.append(one_dim[i])
                i += 1
            result.append(temp)
        return result


        





s = Solution()
print(s.matrixReshape( mat = [[1,2]], r = 1, c = 1))
