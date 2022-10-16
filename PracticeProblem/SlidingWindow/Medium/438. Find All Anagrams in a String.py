from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # if length of p is greater the s we can't find the sub anagrams
        if len(p) > len(s): return [] 
        sCount,pCount = {},{} # hashmap of s and p
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i],0)
            sCount[s[i]] = 1 + sCount.get(s[i],0)
        
        res = [0] if sCount == pCount else [] # check sCount is equal to pCount 
        l = 0 # left pointer
        # we are starting from len(p) charcater cos we have already compute the first len(p) window
        for r in range(len(p),len(s)): 
            sCount[s[r]] = 1 + sCount.get(s[r],0)
            sCount[s[l]] -= 1 # decrement the left most character in the sliding window
            if sCount[s[l]] == 0: # remove the left most charcter.
                sCount.pop(s[l])
            l += 1 # increment the pointer
            if sCount == pCount:
                res.append(l)

        return res
            


s = Solution()
print(s.findAnagrams(s = "abab", p = "ab"))