from typing import List



class Solution:
    
    def arraySign(self, nums: List[int]) -> int:
        total =1
        for x in nums:
            total *= x
        return self.signFunc(total)

    def signFunc(self,n):
        
        if n > 0:
            return 1
        elif n < 0:
            return -1
        else:
            return 0




s= Solution()
print(s.arraySign(nums = [-1,1,-1,1,-1]))