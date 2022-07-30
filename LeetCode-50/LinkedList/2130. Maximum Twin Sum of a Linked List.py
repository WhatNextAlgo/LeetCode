# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = []
        max_val = 0
        if head is None:
            return 0
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        n = len(res)
        for x in range(n//2):
            if res[x] + res[n-1-x] > max_val:
                max_val = res[x] + res[n-1-x]

        return max_val


s = Solution()
print(s.pairSum())