# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(node):
            if not node:return 
            res.append("(")
            res.append(str(node.val))
            if not node.left and node.right:
                res.append("()")
            preorder(node.left)
            preorder(node.right)
            res.append(")")

        preorder(root)
            

        return "".join(res)[1:-1]

    def tree2str1(self, root: Optional[TreeNode]) -> str:
        

        def helper(node):
            if not node:return ""
            if not node.left and not node.right:
                return f"{node.val}"
            
            if not node.right:
                return f"{node.val}({helper(node.left)})"

            return f"{node.val}({helper(node.left)})({helper(node.right)})"

        return helper(root)






s = Solution()
bt = TreeNode(1)
bt.left = TreeNode(2)
bt.right = TreeNode(3)
bt.left.right = TreeNode(4)

print(s.tree2str(bt))