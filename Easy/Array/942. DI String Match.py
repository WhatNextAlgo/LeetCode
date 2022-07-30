def diStringMatch(s):
    res = []
    count_i, count_d =0,len(s)
    for l in s:
        if l == "I":
            res.append(count_i)
            count_i += 1
        elif l == "D":
            res.append(count_d)
            count_d -=1
    res.append(count_i)
    return res


print(diStringMatch(s = "DDI"))