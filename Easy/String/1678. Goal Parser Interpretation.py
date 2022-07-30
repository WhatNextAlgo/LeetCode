

def interpret1(command: str) -> str:
    return command.replace("()","o").replace("(al)","al")

def interpret2(command: str) -> str:
    s = ""
    i = 0
    while i < len(command):
        if command[i]  == "(" and command[i + 1] == ")":
            s += "o"
            i += 2
        elif command[i]  == "(" and command[i + 1] != ")":
            s+="al"
            i += 4
        else:
            s+=command[i]
            i += 1
    return s

def interpret(command: str) -> str:
        str_ = ""
        for i, c in enumerate(command):
            print(i,"--",c)
            if c == "(" and command[i + 1] == ")" and i < len(command) - 1: str_ += "o"
            print(str_)
            if c != "(" and c != ")": str_ += c
            print(str_)
                
        return str_





print(interpret(command = "G()(al)"))