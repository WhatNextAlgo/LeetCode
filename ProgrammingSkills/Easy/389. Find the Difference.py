class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        
        d = {}
        for y in t:
            if y in d:
                d[y]+= 1
            else:
                d[y] = 1
                
        for x in s:
            if x in d:
                d[x] -= 1
            else:
                d[x] = 1
        
        print(d)
        for key,val in d.items():
            if val == 1:
                return  key

s = Solution()
print(s.findTheDifference(s = "a", t = "aa"))
