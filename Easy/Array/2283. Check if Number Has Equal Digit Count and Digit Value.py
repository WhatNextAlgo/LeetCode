def digitCount(num: str) -> bool:
    d = { x:0 for x in range(len(num))}
    for  x in num:
        if int(x) in d:
            d[int(x)] += 1
    print(d)
    for x in range(len(num)):
        print(d[(x)],num[x])
        if d[x] != int(num[x]):
            return False
    return True             

    

print(digitCount(num = "1210"))