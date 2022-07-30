from typing import List


def intersection(nums: List[List[int]]) -> List[int]:
    if nums != []:
        ans = set(nums[0])
        for x in range(1,len(nums)):
            ans &= set(nums[x])
        return sorted(list(ans))
    return []

print(intersection(nums = [[7,34,45,10,12,27,13],[27,21,45,10,12,13]]))