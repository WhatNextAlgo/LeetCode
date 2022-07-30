# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert_bt(node):
            if node is None:
                return None 
            invert_bt(node.left)
            invert_bt(node.right)
            temp = node.left
            node.left = node.right
            node.right = temp

        invert_bt(root)
        return root

            
                








def preorder(node):
    if node is None:
        return None
    print(node.val, end = ' ')
    if node.left is not None:
        preorder(node.left)
    if node.right is not None:
        preorder(node.right)




bt = TreeNode(4)
bt.left =  TreeNode(2)
bt.right =  TreeNode(7)
bt.left.left = TreeNode(1)
bt.left.right = TreeNode(3)
bt.right.left = TreeNode(6)
bt.right.right = TreeNode(9)

s = Solution()
new_bt = s.invertTree(bt)
preorder(new_bt)
        