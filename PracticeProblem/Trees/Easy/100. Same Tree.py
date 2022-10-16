# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # both empty Tree or node it's a same
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


s = Solution()
bt = TreeNode(1)
bt.left = TreeNode(2)
bt.right = TreeNode(3)

bt1 = TreeNode(1)
bt1.left = TreeNode(2)
bt1.right = TreeNode(3)

print(s.isSameTree(bt,bt1))