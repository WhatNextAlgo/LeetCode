from typing import List


def countWords(words1: List[str], words2: List[str]) -> int:
    count =0
    lst = [x for x in words1 if words1.count(x) == 1]
    for x in lst:
        if words2.count(x) ==1 :
            count +=1 
    return count




print(countWords(words1 = ["a","ab"], words2 = ["a","a","a","ab"]))
        