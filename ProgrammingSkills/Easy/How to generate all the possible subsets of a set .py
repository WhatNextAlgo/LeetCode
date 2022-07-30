def possibleSubsets(A= ["a", "b", "c"],N= 3):
    lst = []
    for x  in range(1<<N):
        data = []
        for y in range(N):
            if(x & (1 << y)):
                print(A[y])
                data.append(A[y])
        lst.append(data)
    print(lst)

possibleSubsets()