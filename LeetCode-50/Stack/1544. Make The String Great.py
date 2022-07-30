class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        print(chr(ord('a') - 32),chr(ord('A') + 32))
        for x  in s[1:]:
            if stack != []:
                val  = stack[-1]
                if chr(ord(x) - 32) == val:
                    stack.pop()
                elif chr(ord(x) + 32) == val:
                    stack.pop()
                else:
                    stack.append(x)
            else:
                stack.append(x)
                

        return "".join(stack)



s = Solution()
print(s.makeGood(s = "leEeetcode"))
        