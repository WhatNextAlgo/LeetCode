


from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set() # hash set to check substring is already present or not 
        res = set() # hash set use to store the result cos it will contain duplicates
        for l in range(len(s)-9):
            cur = s[l:l + 10]
            if cur in seen:
                res.add(cur)
            seen.add(cur)

        return list(res)

s = Solution()
print(s.findRepeatedDnaSequences(s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))