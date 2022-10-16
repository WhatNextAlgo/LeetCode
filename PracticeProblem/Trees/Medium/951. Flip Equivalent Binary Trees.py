# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return not root1 and not root2

        if root1.val != root2.val:
            return False
        # check without flip are equal
        a = self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)
        # check second condition with flip are equal
        return a   or self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left)

