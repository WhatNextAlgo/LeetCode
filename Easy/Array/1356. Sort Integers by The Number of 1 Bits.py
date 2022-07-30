def sortByBits(arr):
    arr.sort()
    def conv_bin(n):
        r = 0
        while n > 0:
            r += n%2
            n = n //2
        return r
    
            
    return [y[0] for y in sorted([(x,conv_bin(x)) for x in arr],key=lambda x:x[1])]

print(sortByBits(arr = [0,1,2,3,4,5,6,7,8]))