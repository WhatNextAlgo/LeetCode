import math

def judgeSquareSum1( c: int) -> bool:
    print(10 ** 0.5 )
    print(math.sqrt(10))



def judgeSquareSum( c: int) -> bool:
    for i in range(int(c ** 0.5)+1):
        j = int((c - (i*i))** 0.5)
        print(i,j)
        if (i*i) + (j*j) == c:
            return True
    
    return False
        


print(judgeSquareSum(c = 4))