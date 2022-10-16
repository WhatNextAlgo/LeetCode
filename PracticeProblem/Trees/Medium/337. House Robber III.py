# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [0,0] # [WithRoot,WithoutRoot]

            leftPair = dfs(node.left)
            rightPair = dfs(node.right)
            withRoot = node.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot,withoutRoot]
        return max(dfs(root))



s = Solution()
bt = TreeNode(3)
bt.left = TreeNode(2)
bt.right = TreeNode(3)
bt.left.right = TreeNode(3)
bt.right.right = TreeNode(1)

print(s.rob(bt))
