def prefixCount(words, pref):
    count = 0
    for x in words:
        if x.startswith(pref):
            count +=1

    return count


print(prefixCount(words = ["leetcode","win","loops","success"], pref = "code"))