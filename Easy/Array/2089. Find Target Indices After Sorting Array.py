def targetIndices(nums, target):
    nums.sort()
    lst = []
    for ind,x in enumerate(nums):
        if x == target:
            lst.append(ind)
        elif x > target:
            break
    return lst



print(targetIndices(nums = [1,2,5,2,3], target = 5))