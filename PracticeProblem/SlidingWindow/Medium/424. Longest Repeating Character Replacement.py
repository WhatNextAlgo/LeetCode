class Solution:

    # Solution 1:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 # result of max length after replacement
        l= 0 # left pointer
        countS = {} # hashmap to store freq of character
        maxf = 0 # store the maxf of the charcter
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r],0)
            maxf = max(maxf,countS[s[r]]) # O(1) operation
            while (r - l + 1) - maxf > k: # check windowlen - max of char > k
                countS[s[l]] -= 1 # decreament the left position charcter
                l += 1 # increment the left pointer 
                
            res = max(res, r - l + 1)
        return res
    #Solution 2:
    def characterReplacement1(self, s: str, k: int) -> int:
        res = 0 # result of max length after replacement
        l= 0 # left pointer
        countS = {} # hashmap to store freq of character
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r],0)
            while (r - l + 1) - max(countS.values()) > k: # check windowlen - max of char > k
                countS[s[l]] -= 1 # decreament the left position charcter
                l += 1 # increment the left pointer 
                
            res = max(res, r - l + 1)
        return res




s = Solution()
print(s.characterReplacement(s = "AABABBA", k = 1))