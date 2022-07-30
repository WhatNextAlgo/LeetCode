def removeOuterParentheses(s: str) -> str:
    _str = ""
    outer,inner =0,0
    for x in s:
        if x == "(":
            if outer == 0:
                outer += 1
            else:
                inner += 1
                _str += x
        elif x == ")":
            if inner > 0:
                _str += x
                inner -= 1
            else:
                outer -= 1
    return _str

print(removeOuterParentheses(s = "(()())(())(()(()))"))
