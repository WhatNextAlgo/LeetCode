from typing import List


def maxDistance(nums1: List[int], nums2: List[int]) -> int:
    max_diff = 0
    for index , key in enumerate(nums1):
        left = index
        right = len(nums2)
        while right - left > 1:
            mid = (left + right)  // 2
            if nums2[mid] < key:
                right = mid
            else:
                left = mid
        print(left,index)
        if left - index > max_diff:
            max_diff = left - index

    return max_diff
             

print(maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]))

