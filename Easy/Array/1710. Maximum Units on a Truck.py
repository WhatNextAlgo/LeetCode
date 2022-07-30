def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x:x[1],reverse=True)
    max_val =0
    for x,y in boxTypes:
        if x <= truckSize and truckSize > 0:
            max_val += x * y
            truckSize -=x
        else:
            max_val += truckSize * y
            truckSize -= truckSize
    return max_val


print(maximumUnits( boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))