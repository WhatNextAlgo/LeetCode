from typing import List


def findMedianSortedArrays(nums1, nums2):
    nums1.sort()
    nums2.sort()
    if nums1 == []:
        if nums2 != []:
            mid = int(len(nums2) / 2)
            print(mid)
            if len(nums2) % 2 == 0:
                return (nums2[mid-1] + nums2[mid]) / 2
            else:
                return nums2[mid]

    if nums2 == []:
        if nums1 != []:
            
            mid = int(len(nums1) / 2)
            print(mid)
            if len(nums1) % 2 == 0:
                return (nums1[mid-1] + nums1[mid]) / 2
            else:
                return nums1[mid]

    if nums1 != [] and nums2 != []:
        merge_lst = sorted(nums1 + nums2)  
        print(merge_lst)  
        mid = int(len(merge_lst) / 2)
        print(mid)
        if len(merge_lst) % 2 == 0:
            return (merge_lst[mid-1] + merge_lst[mid]) / 2
        else:
            return merge_lst[mid]

print(findMedianSortedArrays(nums1 = [4,5,6,8,9], nums2 = []))