from typing import List

def countBits(n: int) -> List[int]:
    def convert_to_bin(n):
        bin_lst = []
        while n > 0:
            val = n % 2
            n = n//2
            bin_lst.append(val)
        return bin_lst[::-1]
    return [ sum(convert_to_bin(x)) for x in range(n+1)]

print(countBits(n = 2))
