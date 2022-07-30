from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = []
        for i in range(1,numRows+1):
            C = 1
            data = [C]
            for j in range(1,i):
                C = C * (i - j) // j
                data.append(C)
            lst.append(data)
        return lst
                

                






s = Solution()
print(s.generate(numRows=5))