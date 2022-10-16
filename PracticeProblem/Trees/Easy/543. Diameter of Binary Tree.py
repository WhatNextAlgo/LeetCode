# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0] #global res
        def dfs(node):
            if not root:return -1

            left , right = dfs(node.left),dfs(node.right)
            # D = L + R + 2 
            diameter[0] = max(diameter[0],2 + left + right) 
            # max height from left and right and plus one too it.
            height = 1 + max(left,right)

            return height
        dfs(root)
        return diameter[0]
