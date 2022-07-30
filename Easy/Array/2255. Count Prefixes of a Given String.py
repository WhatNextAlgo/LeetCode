def countPrefixes(words, s):
    count =0
    for word in words:
        if len(word) <= len(s):
            for i in range(len(word)):
                if word[i] != s[i]:
                    break
            else:
                count +=1
    return count


print(countPrefixes(words = ["a","a"], s = "aa"))