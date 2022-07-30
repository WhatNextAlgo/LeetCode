class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for x in s:
            if x != "]":
                stack.append(x)
            elif x == "]":
                if stack:
                    _str = ""
                    num = ""
                    while stack[-1] != "[":
                        poped = stack.pop()
                        _str = poped + _str
                    stack.pop()
                    while stack and stack[-1].isdigit():
                        poped = stack.pop()
                        num = poped + num
                    _str = int(num) * _str
                    stack.append(_str)
                    print(stack)
        return "".join(stack)




s = Solution()
print(s.decodeString( s = "2[abc]10[cd]ef"))
