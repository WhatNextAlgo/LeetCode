def reverseWords1(s: str) -> str:
    lst = []
    for x in s.split():
        l = list(x)
        i = 0
        j = len(l) -1
        for _ in range(len(l)//2):
            l[i], l[j] = l[j],l[i]
            i = i + 1
            j = j - 1
        lst.append("".join(l))
    return " ".join(lst)

def reverseWords(s: str) -> str:
    return " ".join([x[::-1] for x in s.split()])


    


print(reverseWords(s = "God Ding"))