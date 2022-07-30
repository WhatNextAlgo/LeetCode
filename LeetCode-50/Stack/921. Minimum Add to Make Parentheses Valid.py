class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for x in s:
            if stack:
                if stack[-1] != ")" and x != "(" :
                    stack.pop()
                    count -= 1
                else:
                    stack.append(x)
                    count += 1
            else:
                stack.append(x)
                count += 1
        return count
        

s= Solution()
print(s.minAddToMakeValid(s = "()))"))