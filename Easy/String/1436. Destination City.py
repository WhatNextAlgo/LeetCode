from typing import List


def destCity(paths: List[List[str]]) -> str:
    d = {}
    for x in paths:
        d[x[0]] = x[1]
    print(d)

    for x in d.values():
        destination = d.get(x)
        if destination is None:
            return x
        



print(destCity([["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]))