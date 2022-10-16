# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:return [True,0] # reach to leaf node 
            left = dfs(node.left) # left traverse to leaf node
            right = dfs(node.right) # right traverse to leaf node
            #compluting tree is balance or not
            balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1 
            return [balanced,1 + max(left[1],right[1])]
        
        return dfs(root)


s = Solution()
bt = TreeNode(3)
bt.left = TreeNode(9)
bt.right = TreeNode(20)
bt.right.left = TreeNode(15)
bt.right.right = TreeNode(7)
print(s.isBalanced(bt))