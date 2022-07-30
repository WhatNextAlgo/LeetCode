from itertools import product
from typing import List


def allCellsDistOrder(rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
    lst = []
    for x in range(rows):
        for y in range(cols):
            lst.append((x,y))
    
    lst.sort(key=lambda point: abs(point[0] - rCenter) + abs(point[1] - cCenter))
    return lst

print(allCellsDistOrder(rows = 2, cols = 4, rCenter = 1, cCenter = 2))