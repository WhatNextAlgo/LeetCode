# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        mid = self.get_length(head)//2 
        i = 0
        curr = head
        while curr.next and i != mid:
            curr = curr.next
            i = i + 1

        return curr
        
    

    def get_length(self,head):
        if head is None:
            return 0
        count = 0
        curr = head
        while curr:
            count +=1
            curr = curr.next
        return count
        