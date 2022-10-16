class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0 # max lenght of sliding window  
        l = 0 # left pointer
        seen = set() # check if charater exists
        for r in range(len(s)):
            while s[r] in seen:
                # first remove the character
                seen.remove(s[l])
                l += 1  # update the pointer
            seen.add(s[r])

            max_length = max(max_length, r - l + 1) # (r -l + 1) to get length of sliding window 
        return max_length


s  = Solution()
print(s.lengthOfLongestSubstring(s = "abcabcbb"))
print(s.lengthOfLongestSubstring( s = "pwwkew"))
