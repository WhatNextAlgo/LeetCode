from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj= {c : set() for w in words for c in w}
        for i in range(len(words)-1):
            w1 , w2 = words[i] , words[i + 1]
            minLen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit ={} # False = visited , True= current path
        res = []
        def dfs(c):
            if  c in visit:
                return visit[c] # if this is true mean we detect a cycle

            visit[c] = True  # set true mean we added in current path

            for nei in adj[c]:
                if dfs(nei):
                    return True
            
            visit[c] = False # mark it false once we added to current path
            res.append(c)

        for c in adj:
            if dfs(c):
                return False
        
        return "".join(reversed(res))


s = Solution()
print(s.alienOrder(words=["wrt","wrf","er","ett","rftt"]))