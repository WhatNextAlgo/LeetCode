# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def isLeftNode(root):
            if root is None:
                return False
            return not root.left and not root.right
        def getsumOfLeftLeaves(root,isLeft,res):
                if root is None:
                    return
            
                # Check whether this node is a leaf node and is left
                if root.left is None and root.right is None and isLeft == True:
                    res[0] += root.val
            
                # Pass 1 for left and 0 for right
                getsumOfLeftLeaves(root.left, 1, res)
                getsumOfLeftLeaves(root.right, 0, res)
                        

        res = [0]
        getsumOfLeftLeaves(root,0,res)
        return res[0]



bt = TreeNode(0)
bt.left = TreeNode(2)
bt.right = TreeNode(4)
bt.left.left = TreeNode(1)
bt.right.left = TreeNode(3)
bt.right.right = TreeNode(-1)
bt.left.left.left = TreeNode(5)
bt.left.left.right = TreeNode(1)
bt.right.left.right.right = TreeNode(3)
s = Solution()
print(s.sumOfLeftLeaves(bt))
        