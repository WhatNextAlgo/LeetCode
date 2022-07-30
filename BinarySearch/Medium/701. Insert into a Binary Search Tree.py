# Definition for a binary tree node.
from os import name
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)
            return root

        curr = root
        while True:
            if curr.val<=val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break
            else:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
        return root

    


def display(node):
    if not node:
        return None
    print(node.val)
    display(node.left)
    display(node.right)
#[4,2,7,1,3]
bt = TreeNode(4)
bt.left = TreeNode(2)
bt.right = TreeNode(7)
bt.left.left = TreeNode(1)
bt.left.right = TreeNode(3)

s = Solution()
n = s.insertIntoBST(bt,5)
display(n)