# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def display(self,root):
        if not root:return None
        print(root.val,end ="")
        self.display(root.left)
        self.display(root.right)


s = Solution()
bt = TreeNode(4)
bt.left = TreeNode(2)
bt.right = TreeNode(7)
bt.left.left = TreeNode(1)
bt.left.right = TreeNode(3)
bt.right.left = TreeNode(6)
bt.right.right = TreeNode(9)
print("Before")
s.display(bt)
print("After")
print(s.display(s.invertTree(bt)))