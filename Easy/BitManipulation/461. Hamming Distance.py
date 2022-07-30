def hammingDistance(x: int, y: int) -> int:
    def convert_to_bin(n):
        bin_lst = []
        while n > 0:
            val = n % 2
            n = n//2
            bin_lst.append(val)
        return bin_lst[::-1]

    s = convert_to_bin(x)
    t = convert_to_bin(y)
    
    if len(s) > len(t):
        t = ([0] * (len(s)-len(t))) + t
    else:
        s = ([0] * (len(t)-len(s))) + s
    count =0
    for x, y in zip(s,t):
        if x !=y:
            count +=1 
    
    return count



print(hammingDistance(x = 3, y = 1))