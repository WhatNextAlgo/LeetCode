# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root,val):
            if root is None:
                return None

            if root.val == val:
                return root
            
            if root.val > val:
                if root.left is not None:
                    return search(root.left,val)
                else:
                    return None
            elif root.val < val:
                if root.right is not None:
                    return search(root.right,val)
                else:
                    return None



