from typing import List


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    n1 = []
    n2 = []
    for x in set(nums1):
        if x not in nums2:
            n1.append(x)
    for x in set(nums2):
        if x not in nums1:
            n2.append(x)
    return [n1,n2]
print(findDifference([1,2,3,3],[1,1,2,2]))