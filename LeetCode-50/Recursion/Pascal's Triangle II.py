from typing import List

from numpy import arange


class Solution:
    # def getRow(self, rowIndex: int) -> List[int]:
    #     res = []
    
    #     def get_row(i,j):
    #         if j == 1:
    #             return 1
    #         if i == j:
    #             return 1
    #         return get_row(i-1,j-1) + get_row(i-1,j)
    #     for r in range(rowIndex + 1, rowIndex + 2):
    #         for c in range(1,r+1):
    #             res.append(get_row(r,c))
    #     return res

    def getRow(self, rowIndex: int) -> List[int]:
        lst=[1] 
        for i in range(rowIndex): 
            mylist=[] 
            mylist.append(lst[0]) 
            for i in range(len(lst)-1): 
                mylist.append(lst[i]+lst[i+1]) 
            mylist.append(lst[-1]) 
            lst=mylist 
        return lst


s = Solution()
print(s.getRow(rowIndex = 33))