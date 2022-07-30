def uniqueOccurrences(arr):
    d = {}  # Create a dict for storing occurrence of a number 
    for x in arr:
        if x in d:
            d[x] += 1 #increment the count. if it is occurr multiple time
        else:
            d[x] = 1 # for first time
    print(d.values()) # key:value {-3: 3, 0: 2, 1: 4, 10: 1} --> value : [3, 2, 4, 1] 
    lst = list(d.values())
    if len(lst) == len(set(lst)): # if duplicate number is present then len(lst) and set(lst) will not match
        return True
    else:
        return False
    

print(uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))