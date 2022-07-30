
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        counter = 0
        n = 0
        l3 = dummy = ListNode()
        while l1 and l2:
            if (l1.val + l2.val) > 9:
                if counter > 0:
                    counter,n = self.get_counter(l1.val + l2.val + counter)
                    l3.next = ListNode(n)
                else:
                    counter,n = self.get_counter(l1.val + l2.val)
                    l3.next = ListNode(n)
            else:
                if counter > 0:
                    counter,n = self.get_counter(l1.val + l2.val + counter)
                    l3.next = ListNode(n)
                else:
                    counter,n = self.get_counter(l1.val + l2.val)
                    l3.next = ListNode(n)
            #print(l3.val , counter, n)
            

            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        if l1:
            while l1:
                if counter > 0:
                    counter,n = self.get_counter(l1.val+ counter)
                    l3.next = ListNode(n)
                else:
                    counter,n = self.get_counter(l1.val)
                    l3.next = ListNode(n)
                l3 = l3.next
                l1 = l1.next
        if l2:
            while l2:
                if counter > 0:
                    counter,n = self.get_counter(l2.val+ counter)
                    l3.next = ListNode(n)
                else:
                    counter,n = self.get_counter(l2.val)
                    l3.next = ListNode(n)
                l3 = l3.next
                l2 = l2.next
            
        if counter > 0:
            l3.next = ListNode(counter)

        return dummy.next
    
    def get_counter(self,num):
        return  ((num)//10 ,(num)%10)

def display(node):
    curr = node
    while curr:
        print(curr.val,end = " ")
        curr = curr.next
s  = Solution()
list1 = ListNode(2)     
list1.next = ListNode(4)     
list1.next.next   = ListNode(3)    


list2 = ListNode(5)     
list2.next = ListNode(6)     
list2.next.next   = ListNode(4)  

node = s.addTwoNumbers(list1,list2)
display(node)





