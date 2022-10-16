
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        # we  have to alternate to represent the binary string start with '0' and '1'
        alt1 , alt2 = "",""
        for i in range(len(s)):
            alt1 += "0" if i % 2 else "1" 
            alt2 += "1" if i % 2 else "0" 
        
        res = len(s)
        diff1, diff2 =0,0 # flip of two alternate binary string
        l = 0
        for r in range(len(s)):
            #if it is not match then increment the diff
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1

            # if sliding window greater the original window
            # then check left pointer value with alternate string 
            # if it is not match the decrement the diff
            if (r - l + 1) > n:
                if s[l] != alt1[l]:
                    diff1 -= 1
                
                if s[l] != alt2[l]:
                    diff2 -= 1 
                
                l += 1 # increment the left pointer
            #if sliding window  equal to  original window
            if (r - l + 1) == n:
                res = min(res,diff1,diff2) # get the min value
        return res


s = Solution()
print(s.minFlips(s = "111000"))