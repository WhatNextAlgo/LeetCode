from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    for x in matrix:
        if target in x:
            return True
    return False


print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))


