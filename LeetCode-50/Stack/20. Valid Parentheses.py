class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '}': '{', ']': '['}
        stack  = []
        for x in s:
            print(stack)
            if x in "}])":
                if stack and d.get(x) == stack[-1]:
                    stack.pop()
                else:
                    stack.append(x)
            else:
                stack.append(x)
        if not stack:
            return True
        return False

s  = Solution()
print(s.isValid(s = "]"))
