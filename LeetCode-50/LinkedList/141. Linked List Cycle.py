# Definition for singly-linked list.
from operator import truediv
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
            while slow == fast:
                return True
        return False
        