def buildArray(target, n):
    lst = []
    if target == []:
        return ['Push'] * n   
    for x in range(1, max(target) + 1):
        if x in target:
            lst.append("Push")
        else:
            lst.append("Push")
            lst.append("Pop")
    return lst



print(buildArray(target = [1,2], n = 4))