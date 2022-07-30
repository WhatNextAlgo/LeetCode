def sumOddLengthSubarrays(arr):
    lst = []
    for i in range(1,len(arr)+1,2):
        for j in range(len(arr)+1 - i):
            print(lst)
            lst.append(sum(arr[j:j + i]))
    
    return sum(lst)

print(sumOddLengthSubarrays([1,2]))