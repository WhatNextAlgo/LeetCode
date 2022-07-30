def minBitFlips(start: int, goal: int) -> int:
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
    s = convert_to_bin(start)
    t = convert_to_bin(goal)
    
    if len(s) > len(t):
        t = ([0] * (len(s)-len(t))) + t
    else:
        s = ([0] * (len(t)-len(s))) + s
    count =0
    for x, y in zip(s,t):
        if x !=y:
            count +=1 
    
    return count
    



                





print(minBitFlips(start = 35, goal =22))