from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = {}
        for x in (s1.split(" ") + s2.split(" ")):
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        res=[]
        for key,val in d.items():
            if val == 1:
                res.append(key)

        return res




s= Solution()
print(s.uncommonFromSentences(s1 = "apple apple", s2 = "banana"))