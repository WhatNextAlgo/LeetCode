# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def binaryToDecimal(binary) -> int:
            binary1 = binary
            decimal, i, n = 0, 0, 0
            while(binary != 0):
                dec = binary % 10
                decimal = decimal + dec * pow(2, i)
                binary = binary//10
                i += 1
            return decimal
        
        if head is None:
            return 0
        _str = ""
        curr = head
        while curr:
            _str += str(curr.val)
            curr = curr.next
        return binaryToDecimal(int(_str))