from bisect import bisect_left
from typing import List


class Solution:     # Here's the plan:
                    #   1) Make arr, a sorted copy of the list nums.
                    #   2) iterate through nums. For each element num in nums:
                    #       2a) use a binary search to determine the count of elements
                    #         in the arr that are less than num.
                    #       2b) append that count to the answer list
                    #       2c) delete num from arr
                    #   3) return the ans list 
                    #   
                    #   For example, suppose nums = [5,2,6,1] Then arr = [1,2,5,6].
                    #       num = 5 => binsearch: arr = [1,2,/\5,6], i = 2 => ans = [2,_,_,_], del 5
                    #       num = 2 => binsearch: arr = [1,/\2,6],   i = 1 => ans = [2,1,_,_], del 2
                    #       num = 6 => binsearch: arr = [1,/\6],     i = 1 => ans = [2,1,1,_], del 6
                    #       num = 1 => binsearch: arr = [/\1],       i = 0 => ans = [2,1,1,0], del 1

    def countSmaller(self, nums: List[int]) -> List[int]:
        arr, ans = sorted(nums), []     #   <-- 1)
        
        for num in nums:
            i = bisect_left(arr,num)    #   <-- 2a)
            ans.append(i)               #   <-- 2b)
            del arr[i]                  #   <-- 2c)
            
        return ans                      #   <-- 3)