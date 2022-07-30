def maxDepth(s: str) -> int:
    lst  = []
    c  = 0
    max_depth = 0
    for x in s:
        if x == "(":
            lst.append(x)
            c = c + 1
        elif x == ")":
            lst.pop()
            if c > max_depth:
                max_depth = c
            c = c - 1
    return max_depth
            

print(maxDepth(s = "(1)+((2))+(((3)))"))

