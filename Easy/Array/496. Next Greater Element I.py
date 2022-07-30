def nextGreaterElement(nums1, nums2):
    length = len(nums2)
    lst = []
    for x in nums1:
        ind = nums2.index(x)
        if ind ==  length -1:
            lst.append(-1)
        else:
            for i in range(ind,length):
                if nums2[i] > x:
                    lst.append(nums2[i])
                    break
            else:
                lst.append(-1)

    return lst


print(nextGreaterElement([1,3,5,2,4],
[6,5,4,3,2,1,7]))