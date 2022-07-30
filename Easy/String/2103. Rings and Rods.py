def countPoints(rings: str) -> int:
    lst  = [rings[x:x+2] for x in range(0,len(rings),2)]
    d = {}
    for x in lst:
        if x[-1]  in d:
            d[x[-1]] += x[0]
        else:
            d[x[-1]] = x[0]
    count = 0
    for x in d.values():
        if "R" in x and "G" in x and "B" in x:
            count +=1
    return count 

print(countPoints(rings = "G4"))