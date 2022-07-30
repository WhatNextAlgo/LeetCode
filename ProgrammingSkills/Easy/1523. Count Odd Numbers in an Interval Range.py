class Solution:
    def countOdds(self, low: int, high: int) -> int:
        num = (high - low)//2
        if high % 2 != 0 or low % 2 != 0:
            num = num + 1

        return num