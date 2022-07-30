def isSubsequence(s: str, t: str) -> bool:
    i = 0
    for x in range(len(s)):
        for y in range(i,len(t)):
            if s[x] == t[y]:
                i = y + 1
                break 
        else:
            return False
    return True
print(isSubsequence(s = "abc", t = "ahbgdc"))