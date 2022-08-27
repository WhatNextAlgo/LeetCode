# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def __init__(self):
        self.prev = None
    # Solution 1
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root
    
    # Solution 2
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None

            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            if leftTail:
                leftTail.right = root.right
                root.right = root.left
                root.left = None

            last = rightTail or leftTail or root
            return last
        
        dfs(root)
            
