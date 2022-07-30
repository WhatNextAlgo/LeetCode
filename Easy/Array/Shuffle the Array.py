def shuffle(nums,n):
    lst = []
    x, y = nums[:n],nums[n:]
    for i,j in zip(x,y):
        lst.append(i)
        lst.append(j)

    return lst

print(shuffle([1,1,2,2],2))