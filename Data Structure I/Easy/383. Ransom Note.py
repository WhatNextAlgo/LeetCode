class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = {}
        for x in ransomNote:
            rn[x] = 1 + rn.get(x,0)
        
        for x in magazine:
            if x in rn:
                if rn[x] > 0:
                    rn[x] -=1
                if (sum(rn.values()) == 0):
                    return True
        return False



s = Solution()
print(s.canConstruct("fihjjjjei",
"hjibagacbhadfaefdjaeaebgi"))