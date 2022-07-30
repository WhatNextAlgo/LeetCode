def replaceDigits(s: str) -> str:
    _str = ""
    for x in range(0,len(s)):
        if s[x].isdigit():
            _str += chr(ord(s[x-1])+ int(s[x]))
        else:
            _str +=s[x]
    return _str



print(replaceDigits(s = "a1c1e1"))
