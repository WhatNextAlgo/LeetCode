def reversePrefix(word: str, ch: str) -> str:
    if ch not in word:
        return word
    w = list(word)
    ind = w.index(ch)
    i = 0
    j = ind
    while i < j:
        w[i],w[j] = w[j],w[i]
        i = i + 1
        j = j - 1

    return "".join(w)

print(reversePrefix(word = "abcdefd", ch = "z"))