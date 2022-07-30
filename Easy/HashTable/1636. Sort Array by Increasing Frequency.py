from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}
        for  x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] =1
        print(d)
        d1 = {}
        for key,val in d.items():
            if val in d1:
                d1[val] += [key]
            else:
                d1[val] = [key]
        print(d1)

        lst = sorted(list(d1.items()),key=lambda x:x)

        print(lst)
        res = []
        for x in lst:
                res += sorted((x[1] * x[0]),reverse=True)
        return res
                
        


s = Solution()
print(s.frequencySort(nums = [-1,1,-6,4,5,-6,1,4,1]))