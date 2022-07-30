class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        for x in text.split(" "):
            for y in brokenLetters:
                if y in x:
                    break
            else:
                count += 1
        return count 


s = Solution()
print(s.canBeTypedWords(text = "leet code", brokenLetters = "e"))
        