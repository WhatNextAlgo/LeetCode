# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if head is None:
            return None

        curr = dummy= ListNode(0)
        while head is not None:
            if head.val == val:
                head = head.next
                continue
            else:
                curr.next = ListNode(head.val)
            
            curr = curr.next
            head = head.next
        
        return dummy.next

            
            

            


def display(node):
    curr = node
    while curr:
        print(curr.val,end = " ")
        curr = curr.next


s  = Solution()
list1 = ListNode(1)     
list1.next = ListNode(1)   
list1.next.next   = ListNode(6)    
# list1.next.next.next   = ListNode(3)    
# list1.next.next.next.next   = ListNode(4)    
# list1.next.next.next.next.next  = ListNode(6)    

node = s.removeElements(list1,1)         
display(node)
        