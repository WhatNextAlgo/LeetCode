# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return None
        if right == 1:
            return head

        left_node = self.get_node(head,left)
        right_node = self.get_node(head,right)
        while left < right:
            left_node.val,right_node.val = right_node.val,left_node.val
            left_node = left_node.next
            right_node = self.get_node(head,right-1)
            left += 1
            right -=1 

        return head


    def get_node(self,head,index):
        if head is None:
            return None
        curr = head
        count = 1
        while curr and count != index:
            curr = curr.next
            count += 1
        return curr
