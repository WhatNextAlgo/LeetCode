def halvesAreAlike(s: str) -> bool:
    lst = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    mid = len(s)//2
    f_count,s_count = 0,0
    for x in s[:mid]:
        if x in lst:
            f_count += 1
    for y in s[mid:]:
        if y in lst:
            s_count += 1
    if f_count == s_count:
        return True
    return False


print(halvesAreAlike(s = "textbook"))