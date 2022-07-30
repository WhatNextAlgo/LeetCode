class Solution:
    def greatestLetter(self, s: str) -> str:
        # print(chr(ord("A") + 26 + 6))
        # print(ord('a'),ord('Z'))
        sl =[ x for x in s if (ord(x) > 96 and ord(x) < 123)]
        ll =[ x for x in s if (ord(x) > 64 and ord(x) < 91)]
        d = {} 
        for x in ll:
            if chr(ord(x) + 26 + 6) in sl:
                d[x] = chr(ord(x) + 26 + 6)
        if d != {}:
            return max(d.keys())
        else:
            return ""


s = Solution()
print(s.greatestLetter(s = "lEeTcOdE"))