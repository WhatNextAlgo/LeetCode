from typing import List


def reverseString(s: List[str]) -> None:
    n = len(s)
    for x in range(0,n//2):
        s[x],s[n-1-x] = s[n-1-x],s[x]


print(reverseString( s = ["H","a","n","n","a","h"]))
