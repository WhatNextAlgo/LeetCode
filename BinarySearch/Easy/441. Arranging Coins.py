from math import ceil

def arrangeCoins(n):
    rows = ceil(n/2)
    count = 0
    print(rows)
    for x in range(1,rows+1):
        
        if n > 0:
            print(n,x)
            if n - x >= 0:
                count += 1
            n = n -x
    return count 



def arrangeCoins1(n):
    left, right = 0 , n
    while left <= right:
        mid = left + (right - left)//2
        num_com = mid * (mid + 1)//2
        if num_com == n:
            return mid
        elif num_com > n:
            right = mid -1
        else:
            left = mid +1
    return right 

def arrangeCoins1(n):
    left, right = 0 , n
    while right - left >= 0:
        mid = (right + left)//2
        num_com = mid * (mid + 1)//2
        if num_com == n:
            return mid
        elif num_com > n:
            right = mid -1
        else:
            left = mid +1
    return right


print(arrangeCoins(n= 8))