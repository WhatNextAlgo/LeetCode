import re


def specialArray(nums):
    nums.sort()
    def binary_search(target):
        start = 0
        end = len(nums)-1
        while start < end:
            mid = start + (end- start)//2

            if nums[mid] <  target:
                start = mid + 1
            else:
                end = mid
        if nums[end] >= target:
            return len(nums)- end
        else:
            return -1

    for x in range(len(nums)+1):
        if x == binary_search(x):
            return x
    return -1



print(specialArray(nums = [3,5]))