
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val > high:
            return self.trimBST(root.left,low,high)
        
        if root.val < low:
            return self.trimBST(root.right,low,high)
        
        root.left = self.trimBST(root.left,low,high)
        root.right = self.trimBST(root.right,low,high)
        return root


def display(node):
    if not node:return None
    print(node.val)
    display(node.left)
    display(node.right)

s = Solution()
bt = TreeNode(3)
bt.left = TreeNode(0)
bt.right = TreeNode(4)
bt.left.right = TreeNode(2)
bt.left.right.left = TreeNode(1)

print(display(s.trimBST(bt,1,3)))