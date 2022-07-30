from typing import List


def cellsInRange(s: str) -> List[str]:
    lst = s.split(":")
    rows,cols = int(lst[0][-1]),int(lst[1][-1])
    start,end= lst[0][0],lst[1][0]
    res = []
    for x in range(ord(end) - ord(start) + 1):
        for y in range(rows,cols+1):
            res.append(f"{start}{y}")
        start = chr(ord(start) + 1)
   
    return res
    

print(cellsInRange( s = "K5:X9"))