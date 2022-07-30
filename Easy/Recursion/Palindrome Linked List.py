# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    
    
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return None
        
        curr = head
        lst = []
        while curr is not None:
            lst.append(curr.val)
            curr= curr.next
        
        if lst == lst[::-1]:
            return True
        return False