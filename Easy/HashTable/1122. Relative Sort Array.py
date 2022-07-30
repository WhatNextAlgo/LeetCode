from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for x in arr1:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        res = []
        for x in arr2:
            val = d.get(x)
            res += [x] * val
            del d[x]
        if d != {}:
            for x in sorted(list(d.items())):
                res += [x[0]] * x[1]
        return res
        


s = Solution()
print(s.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))