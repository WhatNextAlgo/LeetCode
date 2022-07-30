def areOccurrencesEqual(s: str) -> bool:
    d = {}
    for x in s:
        if x in d:
            d[x] +=1
        else:
            d[x] = 1
    return len(set(d.values())) == 1


print(areOccurrencesEqual(s = "aaabb"))