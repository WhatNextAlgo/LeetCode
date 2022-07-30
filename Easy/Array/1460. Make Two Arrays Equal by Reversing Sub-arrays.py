def canBeEqual( target, arr):
    target.sort()
    arr.sort()
    return True if target == arr else False


print(canBeEqual([1,2,3],[1,2,3]))

