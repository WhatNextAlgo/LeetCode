from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = set(words[0])
        for x in range(1,len(words)):
            res &= set(words[x])
        if res == set():
            return []

        #print(res)

        d = {}
        ans = []
        for y in res:
            rep = float('inf')
            for x in words:
                val = x.count(y)
                if val < rep:
                    rep = val
            ans += [y]*rep
        return ans  
            
        
s = Solution()
print(s.commonChars( words = ["cool","lock","cook"]))
#print(s.commonChars( words = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]))