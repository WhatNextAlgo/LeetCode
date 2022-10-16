# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        
        v1 = root1.val if root1 else 0 #check if root1 exist
        v2 = root2.val if root2 else 0 # check if root2 exit
        root = TreeNode(v1 + v2) # create a new TreeNode and merge the two node
        root.left = self.mergeTrees(root1.left if root1 else None,root2.left if root2 else None) # left traverse
        root.right = self.mergeTrees(root1.right if root1 else None,root2.right if root2 else None) # right traverse
        return root 