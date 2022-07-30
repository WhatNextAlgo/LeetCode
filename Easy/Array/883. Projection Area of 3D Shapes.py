from typing import List


def projectionArea(grid: List[List[int]]) -> int:
    xy = sum( [ sum([n>0 for n in sublist]) for sublist in grid] )
    xz = sum( [ max(sublist) for sublist in grid ] )
    yz = sum( [ max(sublist) for sublist in zip(*grid) ] )
    return xy + xz + yz

print(projectionArea(grid = [[1,2],[3,4]]))