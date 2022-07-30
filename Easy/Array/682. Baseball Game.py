def calPoints(ops):
    lst = []
    for x in ops:
        if x == "C":
            if lst != []:
                lst.pop()
        elif x == "D":
            lst.append(int(lst[-1]) * 2)
        elif x == "+":
            if len(lst) > 1:
                lst.append(int(lst[-1]) + int(lst[-2]))
        else:
            lst.append(int(x))

    return sum(lst)



print(calPoints(ops = ["1","C"]))