from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
    
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                print((w,"= ",m1[w], p,"=",m2[p]), (p, w))
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True
        res= []
        for w in words:
            if match(w):
                res.append(w)
        return res



    



s = Solution()
print(s.findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))