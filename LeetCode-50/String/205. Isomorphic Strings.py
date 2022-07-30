def isIsomorphic(s: str, t: str) -> bool:
    len_match = len(set(s)) == len(set(t))
    if len_match:
        d = {}
        for x in range(len(s)):
            if s[x] not in d:
                d[s[x]] = t[x]
        print(d)
        _str = ""
        for x in s:
            _str += d.get(x)
        if _str == t:
            return True
        return False
    return False

            


print(isIsomorphic(s = "paper", t = "title"))
