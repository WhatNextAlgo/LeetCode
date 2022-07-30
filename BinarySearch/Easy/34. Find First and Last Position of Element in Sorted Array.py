def get_first_index(nums,start_index,target):
    start = start_index
    end = len(nums)
    while start < end:
        mid = start + (end - start)//2
        if nums[mid] >=  target:
            end = mid 
        else:
            start = mid + 1
    return start
    
def searchRange(nums, target):
    first = get_first_index(nums,0,target)
    print(first)
    if target in nums[first:first + 1]:
        return [first,get_first_index(nums,first,target + 1) -1]
    else:
        return [-1.-1]
    


print(searchRange(nums = [3,3,4,5,5,5,5,6], target = 5))
#print(searchRange(nums = [1,1,2,3,4], target = 5))




def searchRange1(nums, target):
    def binary_search(n: int, start: int = None):
        left, right = 0, len(nums)
        if start is not None:
            left = start
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= n:
                right = mid
            else:
                left = mid + 1
        return left
    first_index = binary_search(target)
    print(first_index)
    print(nums[first_index:first_index + 1])
    return [first_index, binary_search(target + 1, first_index) - 1] if target in nums[first_index:first_index + 1] else [
            -1, -1]


#print(searchRange1(nums = [1,2,4,5,6,7], target = 4))