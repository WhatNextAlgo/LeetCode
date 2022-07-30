# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        print(root.val,self.prev.val if self.prev else None)
        root.right = self.prev
        root.left = None
        self.prev = root
        
    
            

def display(node):
    if not node:
        print("null",end= " ")
        return None
    print(node.val, end =" ")
    display(node.left)
    display(node.right)
    


bt = TreeNode(1)
bt.left = TreeNode(2)
bt.right = TreeNode(5)
bt.left.left = TreeNode(3)
bt.left.right = TreeNode(4)
bt.right.right = TreeNode(6)
 
s = Solution()
s.flatten(bt)
display(bt)
        
