def largestAltitude(gain):
    lst = [0]
    for x in range(0,len(gain)):
        lst.append(gain[x] + lst[x])
    return max(lst)
        


print(largestAltitude(gain = [-4,-3,-2,-1,4,3,2]))