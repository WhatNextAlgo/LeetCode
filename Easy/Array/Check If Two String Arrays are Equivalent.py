def arrayStringsAreEqual(word1, word2):
    w1,w2 = "",""
    for x in word1:
        w1 += x
    for y in word2:
        w2 += y
    
    if w1 == w2:
        return True
    return False


print(arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))    