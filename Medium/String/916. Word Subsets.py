from typing import List


class Solution:
    
    def wordSubsets1(self, words1: List[str], words2: List[str]) -> List[str]:
        A ,B = words1,words2
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)
        print(bmax)
        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans

s = Solution()
print(s.wordSubsets(["amazon","apple","facebook","google","leetcode"],
["lo","eo"]))
            

