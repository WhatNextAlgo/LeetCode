def freqAlphabets(s: str) -> str:
    d = {}
    start = ord('a')
    end = ord('z') + 1
    i = ord('i') + 1
    for x in range(start,end):
        if x < i:
            d[str((x-97) + 1)] = chr(x)
        else:
            d[str(x-96) + "#"] = chr(x)
            
    n = len(s)
    j = 0
    _str = ""
    while j < n:
        if j + 2 < n and s[j+2] == "#":
            _str += d.get(s[j : j + 2+1])
            j = j + 3
        else:
            _str += d.get(s[j])
            j = j + 1
    return _str






print(freqAlphabets( s = "1326#"))
