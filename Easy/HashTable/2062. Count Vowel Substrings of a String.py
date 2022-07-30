class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        VOWEL = ('a', 'e', 'i', 'o', 'u')
        count  = 0
        for x in VOWEL:
            if x not in word:
                return count

        k = 0
        while k < len(word):
            a = e = i = o = u = False
            for j in range(k,len(word)):
                if word[j] == 'a':
                    a = True
                elif word[j] == 'e':
                    e = True
                elif word[j] == 'i':
                    i = True
                elif word[j] == 'o':
                    o = True
                elif word[j] == 'u':
                    u = True
                else:
                    a = e = i = o = u = False
                    break
                if a == e == i == o == u == True:
                    count += 1
            k += 1
        return count

        



s = Solution()
print(s.countVowelSubstrings(word = "cuaieuouac"))