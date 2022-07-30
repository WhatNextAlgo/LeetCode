# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None

        before = before_x = ListNode(0)
        after = after_x = ListNode(0)

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            
            head = head.next

        after.next = None
        before.next = after_x.next
        return before_x.next
         




s = Solution()
print(s.partition())
        
