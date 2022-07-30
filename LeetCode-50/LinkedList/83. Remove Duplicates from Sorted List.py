# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head
        before = curr
        after = curr.next
        while after:
            if before.val == after.val:
                before.next = after.next
                after = after.next
            else:
                before = after
                after = after.next
                
        return curr

            
                    
def display(node):
    curr= node
    while curr:
        print(curr.val, end=" " )
        curr = curr.next        

s = Solution()


ll = ListNode(1)
ll.next = ListNode(1)
ll.next.next = ListNode(1)
# ll.next.next.next = ListNode(3)
# ll.next.next.next.next = ListNode(3)

node = s.deleteDuplicates(ll)
display(node)