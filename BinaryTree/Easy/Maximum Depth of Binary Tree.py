# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.max_depth_helper(root)

    def max_depth_helper(self,root):
        if not root:
            return 0

        return 1 + max(self.max_depth_helper(root.left),self.max_depth_helper(root.right))






bt = TreeNode(3)
bt.left =  TreeNode(1)
bt.right =  TreeNode(2)
bt.left.left = TreeNode(4)
bt.right.right = TreeNode(5)

s = Solution()
print(s.maxDepth(bt))