from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, pL, sL = {}, [], len(p), len(s)
        if pL > sL: return []

        # build hashmap
        for ch in p: 
            if ch in hm :
                hm[ch] += 1
            else:
                hm[ch] =1

        for i in range(pL-1):
            if s[i] in hm: hm[s[i]] -= 1
            
            
        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i+pL < sL and s[i+pL] in hm: 
                hm[s[i+pL]] -= 1

            if all(v == 0 for v in hm.values()): 
                res.append(i+1)
                
        return res


s = Solution()
print(s.findAnagrams(s = "abab", p = "ab"))
        