def countGoodTriplets(arr, a, b, c):
    count = 0
    length = len(arr)
    for x in range(length):
        for y in range(x + 1, length):
            for k in range(y + 1, length):
                if abs(arr[x] - arr[y]) <= a and abs(arr[y] - arr[k]) <=b and abs(arr[x] - arr[k]) <= c:
                    count += 1
    return count
    


print(countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))