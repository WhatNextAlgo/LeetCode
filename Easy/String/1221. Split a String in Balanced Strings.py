def balancedStringSplit(s: str) -> int:
    r ,l ,p = 0,0,0
    for x in range(len(s)):
        if s[x] == "R":
            r = r + 1
        else:
            l = l + 1
        
        if r == l:
            p = p + 1

    return p





print(balancedStringSplit(s = "RLRRLLRLRL"))