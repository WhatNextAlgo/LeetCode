def defangIPaddr1(address: str) -> str:
    return "[.]".join(address.split("."))

def defangIPaddr(address: str) -> str:
    return address.replace(".","[.]")
print(defangIPaddr(address = "255.100.50.0"))