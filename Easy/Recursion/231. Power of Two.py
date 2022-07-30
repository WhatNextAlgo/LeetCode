from math import ceil,floor


def isPowerOfTwo( n: int) -> bool:

    return n and (not (n & (n-1)))

print(isPowerOfTwo(n = 4))