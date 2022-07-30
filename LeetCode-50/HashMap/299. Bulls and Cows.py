class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        lst = [0] * 10
        for s,g in zip(secret,guess):
            if s == g:
                bulls += 1
            else:
                lst[int(s)] += 1
                lst[int(g)] -= 1
        cows = len(secret)- bulls - sum(x for x in lst if x > 0)
        return f"{str(bulls)}A{str(cows)}B"



                    

s = Solution()
print(s.getHint(secret = "1122", guess = "1222"))