from typing import List


def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
    target = []
    for x,y in zip(index,nums):
        target.insert(x,y)

    return target



print(createTargetArray(nums = [1], index = [0]))