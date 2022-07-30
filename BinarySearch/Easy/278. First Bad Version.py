def firstBadVersion(n):
    start = 1
    end = n
    ans = 1
    while end -start >= 0:
        mid = (start + end)//2

        b = isBadVersion(mid)
        if b:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1
    return ans



def isBadVersion(n):
    if n in [3,4,5,6]:
        return True
    return False

print(firstBadVersion(6))