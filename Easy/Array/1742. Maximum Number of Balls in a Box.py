class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d={}
        max_ball =0
        for ball in range(lowLimit, highLimit+1):
            count=0
            while ball>0:
                count += (ball%10)
                ball = ball//10
            if count in d:
                d[count] +=  1
            else:
                d[count] = 1
            max_ball = max(max_ball, d[count]) 
        return max_ball

s =Solution()
print(s.countBalls(lowLimit = 5, highLimit = 15))