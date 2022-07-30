

def countPrimeSetBits(left: int, right: int) -> int:
    def convert_to_bin(n):
        bin_lst = []
        while n > 0:
            val = n % 2
            n = n//2
            bin_lst.append(val)
        return bin_lst[::-1]

    def isPrimeNum(num):
        k = 0
        for i in range(2, num//2 + 1):
            if num % i == 0:
                k = k + 1
        if k <=0:
            return True
        
        return False
    count = 0
    for x in range(left,right +1):
        val = sum(convert_to_bin(x))
        if val > 1 and isPrimeNum(val):
            count +=1
    return count


print(countPrimeSetBits(left = 6, right = 10))