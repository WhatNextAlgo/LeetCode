# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(root):
            if root is None:
                return None
            curr = root
            while curr and curr.next:
                curr.val, curr.next.val = curr.next.val,curr.val
                curr = curr.next.next

        swap(head)
        return head


def display(lst):
    curr = lst
    while curr:
        print(curr.val)
        curr = curr.next



ll = ListNode(1)
ll.next =  ListNode(2)
ll.next.next =  ListNode(3)
ll.next.next.next = ListNode(4)


s = Solution()
s.swapPairs(ll)
display(s.swapPairs(ll))
                
        
        