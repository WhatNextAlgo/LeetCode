from typing import List


def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr.sort()
    return len(set([arr[x] -arr[x-1] for x in range(1,len(arr))])) == 1
        
        

print(canMakeArithmeticProgression(arr = [1,2,4]))