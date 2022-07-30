


import random 


def generateTheString(n: int) -> str:
    _str = ""
    random_num = random.randrange(98,123)
    print(random_num)
    if n > 0:
        if n % 2 == 0:
            _str += (str(chr(97)) * (n -1)) + chr(random_num)
        else:
            _str += chr(random_num) * n
    return _str



print(generateTheString(n = 4))