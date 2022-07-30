from typing import List


def numOfStrings(patterns: List[str], word: str) -> int:
    count = 0
    for x in patterns:
        if x in word:
            count +=1 
    return count

print(numOfStrings(patterns = ["a","a","a"], word = "ab"))