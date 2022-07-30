def checkIfPangram(sentence: str) -> bool:
    for x in range(97,123):
        if chr(x) not in sentence:
            return False
    return True


print(checkIfPangram(sentence = "leetcode"))