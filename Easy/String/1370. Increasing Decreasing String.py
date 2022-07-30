def sortString(s: str) -> str:
    d = {}
    for x in s:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    _str = ""
    lst = sorted([[x,d[x]]for x in d])
    
    for x in range(0,len(s)//2+1):
        for i in range(0,len(lst)):
            if lst[i][1] > 0:
                _str +=lst[i][0]
                lst[i][1] -=1
                
        for i in range(len(lst)-1,-1,-1):
            if lst[i][1] > 0:
                _str +=lst[i][0]
                lst[i][1] -=1
    return _str
        
    
    


print(sortString(s = "aaaabbbbcccc"))