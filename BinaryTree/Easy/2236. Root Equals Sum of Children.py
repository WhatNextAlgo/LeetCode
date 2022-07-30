# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        total = 0
        def get_total(root):
            nonlocal total
            if root is None:
                return 0
            if root.left is not None:
                total += root.left.val
                get_total(root.left)
                
            if root.right is not None:
                total += root.right.val
                get_total(root.right)
        
        get_total(root)
        if total == root.val:
            return True
        
        return False
            