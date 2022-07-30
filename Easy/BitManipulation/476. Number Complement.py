def findComplement(num: int) -> int:
    def convert_to_bin(n):
        bin_lst = []
        while n > 0:
            val = n % 2
            n = n//2
            bin_lst.append(val)
        return bin_lst[::-1]
    
    def bin_to_dec(s):
        n = len(s)
        res = 0
        for x in range(n-1,-1,-1):
            res += (s[x] * (2 ** (n-1-x)))
        return res
    
    return bin_to_dec([ 0 if x == 1 else 1 for x in convert_to_bin(num)])
    

print(findComplement(num = 1))