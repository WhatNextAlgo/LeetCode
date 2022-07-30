from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        lst  = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        for x in words:
            for y in lst:
                for z in set(x.lower()):
                    if z not in y:
                        break
                else:
                    res.append(x)
                    break
        return res






s = Solution()
print(s.findWords( words = ["adsdf","sfd"]))
