from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_spend = 0
        while tickets[k] != 0:
            for x in range(len(tickets)):
                if tickets[x] != 0 and tickets[k] != 0:
                    tickets[x] -=1
                    time_spend +=1
            
        return time_spend




s = Solution()
print(s.timeRequiredToBuy(tickets = [2,3,2], k = 2))
        