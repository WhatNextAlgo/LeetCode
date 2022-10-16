class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : return ""

        countT, window = {},{} #Hashmap for t and sliding window
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        have,need = 0,len(countT)
        res, resLen = [-1,-1],float('infinity') # res will store the index of sliding window
        l = 0 # left pointer
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                #update our result
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1
                #pop from the left of our window until we met the condition of have == need
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:l + r] if resLen != float('infinity') else ""



s = Solution()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(s.minWindow(s = "a", t = "aa"))
