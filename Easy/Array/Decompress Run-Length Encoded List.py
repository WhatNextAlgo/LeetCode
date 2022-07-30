def decompressRLElist(nums):
    lst = []
    for x in range(0,len(nums),2):
        for _ in range(nums[x]):
            lst.append(nums[x + 1])

    return lst


print(decompressRLElist([1,1,2,3]))

