def truncateSentence(s: str, k: int):
    lst = s.split()
    return " ".join(lst[:k])


print(truncateSentence(s = "chopper is not a tanuki", k = 5))