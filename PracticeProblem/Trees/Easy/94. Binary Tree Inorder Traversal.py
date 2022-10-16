# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res



s = Solution()
bt = TreeNode(1)
bt.right = TreeNode(2)
bt.right.left = TreeNode(3)


print(s.inorderTraversal(bt))
