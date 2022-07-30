def replaceElements(arr):
    for x in range(1,len(arr)):
        print(arr[x:])
        arr[x-1] = max(arr[x:])
    
    arr[-1] =-1
    return arr
        



print(replaceElements(arr = [400]))