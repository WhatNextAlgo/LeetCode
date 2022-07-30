from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1,d2 = {},{}
        for x in nums1:
            if x in d1:
                d1[x] += 1
            else:
                d1[x] = 1
        for x in nums2:
            if x in d2:
                d2[x] += 1
            else:
                d2[x] = 1

        s = set(nums1) & set(nums2)
        res = []
        for x in s:
            count = min(d1.get(x),d2.get(x))
            for _ in range(count):
                res.append(x)

        return res