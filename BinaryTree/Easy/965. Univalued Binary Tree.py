# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        check = root.val
        is_univaltree = True
        def is_univaltree_helper(root):
            if root is None:
                return None
            if root.val != check:
                is_univaltree = False
            if root.left is not None:
                is_univaltree_helper(root.left)

            if root.right is not None:
                is_univaltree_helper(root.right)


        is_univaltree_helper(root)
        return is_univaltree

    # def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
    #         left_node = (not root.left or root.val == root.left.val
    #                 and self.isUnivalTree(root.left))
    #         right_node = (not root.right or root.val == root.right.val
    #                 and self.isUnivalTree(root.right))
    #         return left_node and right_node
        