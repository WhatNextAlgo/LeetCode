def xorOperation1(n: int, start: int) -> int:
    lst = [ start + 2 * i for i in range(n)]
    ans = 0
    for x in lst:
        ans^=x
    return ans

def xorOperation(n: int, start: int) -> int:
    ans = 0
    for i in range(n):
        ans^=(start + 2 * i)
    
    return ans

print(xorOperation(n = 5, start = 0))