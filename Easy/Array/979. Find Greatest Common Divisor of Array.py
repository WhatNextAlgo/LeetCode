from typing import List
def gcd(a,b):
    if a== 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a

    if a > b:
        return gcd(a-b,b)
    return gcd(a,b-a)

def findGCD(nums):
    def gcd(a,b):
        if a== 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a

        if a > b:
            return gcd(a-b,b)
        return gcd(a,b-a)
    nums.sort()
    
    return gcd(nums[0],nums[-1])


print(findGCD(nums = [2,5,6,9,10]))