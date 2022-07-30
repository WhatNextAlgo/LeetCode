from typing import List


def checkIfExist(arr: List[int]) -> bool:
    for x in arr:
        if x * 2 in arr:
            if x == 0:
                if arr.count(x) < 2:
                    continue
            return True
    return False


    
    
    
print(checkIfExist(arr = [-20,8,-6,-14,0,-19,14,5]))