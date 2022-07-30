from hashlib import new


def twoOutOfThree(nums1, nums2, nums3):
    lst  = [nums1,nums2,nums3]
    length = len(lst)
    new_lst= [list(set(lst[x]) & set(lst[y])) for x in range(length) for y in range(x +1,length)]
    l = []
    for x in new_lst:
        l += x
    return list(set(l))


print(twoOutOfThree(nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]))