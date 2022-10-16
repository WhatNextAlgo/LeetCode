from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Hashmap on stickers
        stickCount = []
        for i, s in enumerate(stickers):
            stickCount.append({})
            for c in s:
                stickCount[i][c] = 1 + stickCount[i].get(c,0)
        
        dp = {} # key = subseq of target | val = min num of stickers

        def dfs(t,stick):
            if t in dp:
                return dp[t]

            res = 1 if stick else 0
            remainT = ""
            for c in t:
                if c in stick and stick[c] > 0:
                    stick[c] -= 1
                else:
                    # remaining character which are not mapped
                    remainT += c
            # remainT is not empty then run the dfs on remainT
            if remainT != "":
                used = float("inf")
                for s in stickCount:
                    if remainT[0] not in s:
                        continue
                    used = min(used,dfs(remainT,s.copy()))
                    # cache the remainT
                dp[remainT] = used
                # update the result
                res += used


            return res

            

        res = dfs(target,{})
        return res if res != float('inf') else -1

s = Solution()
print(s.minStickers(stickers = ["with","example","science"], target = "thehat"))