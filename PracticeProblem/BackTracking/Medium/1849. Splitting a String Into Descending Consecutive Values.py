class Solution:
    def splitString(self, s: str) -> bool:

        def dfs(index,prev):
            if index == len(s):
                return True
            for j in range(index,len(s)):
                val = int(s[index:j + 1])
                if val + 1 == prev and dfs(j + 1,val):
                    return True
            
            return False


        # we can't go at the last cos atleast we want two split
        for i in  range(len(s) - 1):
            val = int(s[:i + 1]) # init we have not restriction to calculate the value
            if dfs(i + 1,val):return True

        return False

s = Solution()
print(s.splitString(s = "1234"))
print(s.splitString(s = "009089"))
print(s.splitString(s = "050043"))
