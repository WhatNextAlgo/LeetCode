class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = {}
        t_count = {}
        for x in range(len(s)):
            s_count[s[x]] = 1 + s_count.get(s[x],0)
            t_count[t[x]] = 1 + t_count.get(t[x],0)
        
        for x in s_count:
            if s_count[x] != t_count.get(x,0):
                return False
        return True