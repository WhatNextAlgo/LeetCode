class Solution:
    def judgeCircle(self, moves: str) -> bool:
        v, h= 0,0
        for x in moves:
            if x == "U":
                v += 1
            elif x == "D":
                v -=1
            elif x == "R":
                h +=1
            elif x == "L":
                h -=1
            else:
                print("Invalid key")
        if v == 0 and h == 0:
            return True
        return False 




s  = Solution()
print(s.judgeCircle(moves = "UDLR"))
        