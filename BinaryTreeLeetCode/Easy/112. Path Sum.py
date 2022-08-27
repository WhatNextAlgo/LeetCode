# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node,curSum):
            if not node:
                return False

            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum

            return (dfs(node.left,curSum) or
            dfs(node.right,curSum))

        return dfs(root, 0)


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def isLeaf(root):
            return True if not root.left and not root.right else False
        
        if root and isLeaf(root) and targetSum - root.val == 0:
            return True
        elif root and isLeaf(root) and targetSum - root.val < 0:
            return False
        elif root:
            next_target = targetSum - root.val
            left = self.hasPathSum(root.left, next_target)
            right = self.hasPathSum(root.right, next_target)
            return left if left else right