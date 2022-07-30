def peakIndexInMountainArray(arr):
    n = len(arr)
    for x in range(n):
        if arr[x] > arr[x+1]:
            return x
        
        if arr[n-1-x] > arr[n-2 -x]:
            return n-1-x

def peakIndexInMountainArray(arr):
    max_val = max(arr)
    return arr.index(max_val)



    
    
print(peakIndexInMountainArray(arr = [0,1,3,4,10,0]))