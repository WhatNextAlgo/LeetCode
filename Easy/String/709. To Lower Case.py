def toLowerCase(s: str) -> str:
    a = ord('a')
    A = ord('A')
    return "".join([chr(a + (ord(x) - A)) if ord(x) in list(range(65,91))  else x for x in s ])


    
    
    
print(toLowerCase(s = "Hello@[]"))