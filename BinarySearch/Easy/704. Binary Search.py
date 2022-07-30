def search(nums, target):
    end = len(nums) -1
    start = 0

    while end - start >= 0:
        mid = (start + end)//2
        print(mid)

        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid -1
        else:
            return mid
    return -1
def binary_search(alist, start,end,key):
    if end - start <= 0:
        return -1

    mid = (start + end)//2
    if alist[mid] > key:
        return binary_search(alist,start, mid-1,key)
    elif alist[mid] < key:
        return binary_search(alist,mid + 1, end,key)
    else:
        return mid

def search1(nums,target):
    return binary_search(nums,0,len(nums),target)

print(search1(nums = [-1,0,3,5,9,12], target = 12))

        