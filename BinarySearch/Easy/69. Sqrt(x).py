def mySqrt(x):
    start = 1
    end = x
    ans =0

    while end - start >= 0:
        mid = (start + end)//2

        if mid * mid == x:
            return mid

        if mid * mid < x:
            start = mid + 1
            ans = mid
        else:
            end = mid -1

    return ans

print(mySqrt(8))