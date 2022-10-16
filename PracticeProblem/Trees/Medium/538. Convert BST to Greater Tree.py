# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0
        def dfs(node):
            nonlocal curSum
            if not node:
                return 
            dfs(node.right)
            temp = node.val # original value
            node.val += curSum # update the node value
            curSum += temp # update the curSum 

            dfs(node.left)
        dfs(root)
        return root

def display(node):
    if not node:return None
    display(node.left)
    print(node.val,end = " ")
    display(node.right)

s = Solution()
bt = TreeNode(4)
bt.left = TreeNode(1)
bt.right = TreeNode(6)
bt.left.left = TreeNode(0)
bt.left.right = TreeNode(2)
bt.left.right.right = TreeNode(3)
bt.right.left = TreeNode(5)
bt.right.right = TreeNode(7)
bt.right.right.right = TreeNode(8)

display(s.convertBST(bt))
