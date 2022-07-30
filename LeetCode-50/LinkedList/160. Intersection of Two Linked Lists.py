# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        B = headB
        while A != B: 
            # Once both of them go through reassigning,
            # they will be equidistant from the collision point.
            
            # When A reaches the end of a list, then
            # reassign it to the headB.
            if A is None:
                A = headB
            else:
                A = A.next
            
            # When B reaches the end of a list, then
            # reassign it to the headA.
            if B is None:
                B = headA
            else:
                B = B.next 
        return A