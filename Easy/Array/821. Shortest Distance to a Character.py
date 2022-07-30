def shortestToChar(s,c):
    lst = []
    m = len(s)
    l = 0
    r = 0
    while r < len(s):
        if s[r] == c and s[l] != c:
            lst.append(min(abs(r - l), abs(m - l)))
            l = l + 1
        elif s[r] == c and s[l] == c and r == l:
            lst.append(0)
            r = r + 1
            m = l
            l = l + 1
            print(m,r,l)
        else:
            r = r + 1
    if len(s) == len(lst):
        return lst
    else:
        last = 1
        for x in range(len(s)-len(lst)):
            lst.append(last)
            last += 1
        return lst
        

          


print(shortestToChar(s = "aaba", c = "b"))