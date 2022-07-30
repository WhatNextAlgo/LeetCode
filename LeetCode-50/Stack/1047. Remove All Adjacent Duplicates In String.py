class Solution:
    def removeDuplicates(self, s: str) -> str:
        unique = []
        for x in s:
            if x in unique:
                if x == unique[-1]:
                    unique.pop()
                else:
                    unique.append(x)
            else:
                unique.append(x)
        return "".join(unique)
            

if __name__== "__main__":
    s = Solution()
    print(s.removeDuplicates(s = "abbbabaaa"))
