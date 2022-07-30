# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        before = None
        curr = head
        after = curr.next
        while after:
            curr.next = before
            before = curr
            curr = after
            after = after.next
        curr.next = before
        head = curr
         