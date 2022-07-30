def restoreString(s, indices):
    tuple_lst = [ (x,y) for x, y in zip(list(s),indices)]
    tuple_lst.sort(key=lambda x: x[1])
    return "".join([x for x , y in tuple_lst])
    


print(restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
print(list("codeleet"))