def minimumAbsDifference(arr):
    if arr != []:
        arr.sort()
        lst = []
        for x in range(len(arr)-1):
            if arr[x+1] > arr[x]:
                lst.append(([arr[x],arr[x+1]],arr[x+1]-arr[x]))
            else:
                lst.append(([arr[x],arr[x+1]],arr[x]-arr[x+1]))
        
        min_val = min(lst,key=lambda x:x[1])[1]
        return [x[0] for x in lst if x[1] == min_val]
    


print(minimumAbsDifference(arr = [3,8,-10,23,19,-4,-14,27]))