from gettext import ngettext
from itertools import product


def mergeAlternately( word1: str, word2: str) -> str:
    max_len = len(word1) if len(word1) > len(word2) else len(word2)
    lst = []
    for x in  range(max_len):
        if x < len(word1):
            lst.append(word1[x])
        
        if x < len(word2):
            lst.append(word2[x])

    return "".join(lst)



print(mergeAlternately("ab","pqrs"))