# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     curr = dummy =head
    #     prev = None
    #     while curr :
    #         if curr.val == 0 and curr.next:
    #             temp = curr.next
    #             total = curr.val
    #             curr = temp
    #             while curr and curr.val != 0:
    #                 total += curr.val
    #                 curr = curr.next
    #             print("total ",total)
    #             if total > 0 and curr and curr.val == 0:
    #                 temp.val = total
    #                 temp.next = curr
    #                 curr = temp
    #         else:
    #             curr = curr.next

    #     return dummy

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        before =None
        after = curr.next
        while after:
            print(curr.val,after.val)
            
            if after.val == 0:
                if before is None:
                    before = curr
                else:
                    before = before.next
                
                curr = curr.next
                print("curr",curr.val)
                curr.val = 0
            else:
                curr.val += after.val
            after = after.next
        before.next = None
        return head




                 


        

    def mergeNodes1(head):
        left = head
        prev = None #this is the third pointer to mark the end node Null when loop ends,
		            #it is always one behind the left node
        right = head.next
        while right:
            if right.val == 0:
                if prev == None:
                    prev = left
                else:
                    prev = prev.next
                left = left.next
                left.val = 0 # Since the node might have some prev value, we need to make reset it to 0
            else:
                left.val += right.val
            right = right.next
        prev.next = None
        return head

            


def display(node):
    curr = node
    while curr:
        print(curr.val,end = " ")
        curr = curr.next

s  = Solution()
list1 = ListNode(0)     
list1.next = ListNode(1)   
list1.next.next   = ListNode(6)    
list1.next.next.next   = ListNode(0)    
list1.next.next.next.next   = ListNode(4)    
list1.next.next.next.next.next  = ListNode(6)    
list1.next.next.next.next.next.next  = ListNode(0) 
list1.next.next.next.next.next.next.next  = ListNode(1) 
list1.next.next.next.next.next.next.next.next  = ListNode(2) 
#list1.next.next.next.next.next.next.next.next.next  = ListNode(0) 

node = s.mergeNodes(list1)
display(node)



                    
                




print
        