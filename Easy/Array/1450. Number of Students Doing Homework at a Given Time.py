def busyStudent(startTime, endTime, queryTime):
    count = 0
    for x,y in zip(startTime,endTime):
        if queryTime in list(range(x,y+1)):
            count +=1

    return count

print(busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4))
