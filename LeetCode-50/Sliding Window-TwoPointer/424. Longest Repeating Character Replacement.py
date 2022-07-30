class Solution:
    # def characterReplacement(self, s: str, k: int) -> int:
    #     d = { x: 0 for x in list(set(s))}
    #     res = 0
    #     l =0
    #     for r in range(len(s)):
    #         d[s[r]] = 1 + d.get(s[r],0)
    #         if  (r - l + 1) - max(d.values()) > k:
    #             d[s[l]] -= 1
    #             l = l + 1
    #         res  = max(res, r - l + 1)

    #     return res

    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        res = 0
        l =0
        maxf = 0
        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r],0)
            maxf = max(maxf,d[s[r]])
            if  (r - l + 1) - maxf > k:
                d[s[l]] -= 1
                l = l + 1
            res  = max(res, r - l + 1)

        return res




s= Solution()
print(s.characterReplacement(s = "AABABBA", k = 1))
        
