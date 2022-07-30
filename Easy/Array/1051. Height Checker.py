def heightChecker(heights):
    expected = sorted(heights)
    count =0 
    for x,y in zip(heights,expected):
        if x != y:
            count +=1
    return count


print(heightChecker(heights = [1,2,3,4,5]))