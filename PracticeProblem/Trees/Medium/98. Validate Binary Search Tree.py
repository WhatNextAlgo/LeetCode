# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node,leftBound,rightBound):
            if not node: # empty BST is a BST
                return True

            if not (node.val < rightBound and node.val > leftBound):
                return False
            # for left : -inf (left bound) < node.left < node.val(parent root node)
            # for right: node.val(parent root node) < node.right < inf (right Bound)
            return (valid(node.left,leftBound,node.val) and
                    valid(node.right,node.val,rightBound)) 
                    


        return valid(root,float("-inf"),float('inf'))