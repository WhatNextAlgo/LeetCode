from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq1(self, s: str, words: List[str]) -> int:
        def matchSubSeq(ss:str) -> bool:
            t = s[:]
            for c in ss:
                if c in t:
                    t = t[t.find(c)+1:]
                else:
                    return False
            return True
        count = 0
        for w in words:
            if matchSubSeq(w):
                count = count + 1
        return count
    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def matchSubSeq(ss:str) -> bool:
            cnt = 0
            i = 0
            for c in ss:
                while i < len(s):
                    if s[i] == c:
                        i += 1
                        cnt += 1
                        break
                    else:
                        i += 1
            if cnt == len(ss):
                 return True
            return False
            
        count = 0
        d = set()
        for w in words:
            if w not in d:
                d.add(w)
                if matchSubSeq(w):
                    count = count + 1
            elif w in d:
                count = count + 1
        return count


s = Solution()
print(s.numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))
print(s.numMatchingSubseq(s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))

