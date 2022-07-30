def mostWordsFound(sentences):
    return max([len(x.split()) for x in sentences])

print(mostWordsFound(["please wait", "continue to fight", "continue to win"]))