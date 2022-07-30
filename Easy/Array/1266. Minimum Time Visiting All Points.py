def minTimeToVisitAllPoints(points):
    n = len(points)
    sec = 0
    for x in range(1,n):
        d1 = points[x][0] - points[x-1][0]
        d2 = points[x][1] - points[x-1][1]
        sec += max(abs(d1),abs(d2))

    return sec
    

        

print(minTimeToVisitAllPoints(points = [[3,2],[-2,2]]))