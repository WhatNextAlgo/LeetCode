from typing import List


def search(nums: List[int], target: int) -> int:
    try:
        res = nums.index(target)
        return res
    except:
        return -1



print(search(nums = [4,5,6,7,0,1,2], target = 0))
