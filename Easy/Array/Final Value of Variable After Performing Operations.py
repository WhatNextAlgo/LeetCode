
def finalValueAfterOperations(operations):
    res = 0
    for x in operations:
        s = x[1]
        if s == '-':
            res = res -1
        elif s == '+':
            res = res + 1

    return res


print(finalValueAfterOperations(["--X","X++","X++"]))

