def sumZero(n):
    lst = []
    if n == 1:
        return [0]  
    if n % 2 == 0:
        for x in range(1,n//2 + 1):
            lst.append(x)
            lst.append(-x)
    else:
        lst = [0]
        for x in range(1,n//2 + 1):
            lst.append(x)
            lst.append(-x)
    return lst
    



print(sumZero(n = 2))