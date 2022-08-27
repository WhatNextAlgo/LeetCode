# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #new binary Tree
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0

        root = TreeNode(v1 + v2)
        root.left = self.mergeTrees(root1.left if root1 else None,root2.left if root2  else None)
        root.right = self.mergeTrees(root1.right if root1 else None,root2.right if root2  else None)
        return root

    #inplace 
    def mergeTrees1(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge_node(node1,node2):
            if not node1:
                return node2
            if not node2:
                return node1

            node1.val += node2.val
            node1.left = merge_node(node1.left,node2.left)
            node1.right = merge_node(node1.right,node2.right)
            return node1
        
        return merge_node(root1,root2)