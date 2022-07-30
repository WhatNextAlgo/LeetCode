def guessNumber(n):
    start = 1
    end = n

    while end - start >=0:
        mid = (start + end)//2

        r = guess(mid)
        if r == -1:
            end = mid -1
        elif r == 1:
            start = mid + 1
        else:
            return mid

    return -1

def guess(p):
    pass