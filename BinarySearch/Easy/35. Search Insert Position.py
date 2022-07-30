def searchInsert(nums, target):
    index= 0
    pos= 0
    while index < len(nums):
        if nums[index]== target:
            return index
        elif target > nums[index]:
            pos = index+1
            index = index+1
        else:
            break
    return pos
  


print(searchInsert(nums = [1,3,5,6] , target = 4))
