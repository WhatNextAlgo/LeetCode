from typing import List


def findKthPositive(arr: List[int], k: int) -> int:
    lst = []
    i = 1
    while len(lst) <k + 1:
        if i not in arr:
            lst.append(i)
            i = i + 1
        else:
            i = i + 1
    return lst[k-1]



    


print(findKthPositive(arr = [1,2,3,4], k = 2))