
def countConsistentStrings(allowed,words):
    count = 0
    for word in words:
        if set(word).issubset(set(allowed)):
            count +=1
    return count



print(countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))