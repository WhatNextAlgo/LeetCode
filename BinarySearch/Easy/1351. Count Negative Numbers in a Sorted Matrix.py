from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([1 for x in grid for y in x if y < 0])