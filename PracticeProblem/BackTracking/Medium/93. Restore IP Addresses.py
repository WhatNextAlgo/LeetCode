from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 256 choices for each of the 4 splots But ..
        # The Order of s stays same,
        # we just place the "." between

        res = []
        if len(s) > 12:
            return res

        def backtrack(i,dots,curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return 
            if dots > 4:
                return
             # min((i + 3),len(s)) cos it can be out of bounced
             #i = start and j = end pointer
            for j in range(i,min((i + 3),len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(j + 1,dots + 1,curIP + s[i:j+1] + ".")

        backtrack(0,0,"")
        return res



s = Solution()
print(s.restoreIpAddresses(s = "25525511135"))