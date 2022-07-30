class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for x in s:
            if x in d:
                d[x] += 1
            else:
                d[x] =1
        for x in range(len(s)):
            if d[s[x]] == 1:
                return x
        return -1