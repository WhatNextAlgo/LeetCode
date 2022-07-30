class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d = {x:0 for x in set(word1 + word2)}
        for x in word1:
            if x in d:
                d[x] += 1
            else:
                d[x] =1
        for x in word2:
            if x in d:
                d[x] -= 1
            else:
                d[x] = -1
        for x in d:
            if abs(d[x]) >3:
                return False
        return True

s = Solution()
print(s.checkAlmostEquivalent(word1 = "cccddabba", word2 = "babababab"))