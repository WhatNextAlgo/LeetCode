# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
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
        


    





bt = TreeNode(5)
bt.left =  TreeNode(4)
bt.right =  TreeNode(8)
bt.left.left = TreeNode(11)
#bt.left.right = TreeNode(5)
bt.right.left = TreeNode(13)
bt.right.right = TreeNode(4)
bt.left.left.left = TreeNode(7)
bt.left.left.right = TreeNode(3)
bt.left.left.right.right = TreeNode(2)
bt.right.right.right  = TreeNode(1)



s = Solution()
print(s.hasPathSum(bt,22))