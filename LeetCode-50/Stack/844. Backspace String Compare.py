from typing import List


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_stack(string:str)-> List[str]:
            stack = []
            for x in string:
                if x != "#":
                    stack.append(x)
                else:
                    if stack:
                        stack.pop()

            return stack
        
        return get_stack(s) == get_stack(t)


s = Solution()
print(s.backspaceCompare(s = "a#c", t = "b"))