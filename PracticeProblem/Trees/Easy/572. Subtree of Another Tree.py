# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot : return True 

        if not root: return False

        if self.isSameTree(root,subRoot):
            return True

        return (self.isSubtree(root.left,subRoot) or
                self.isSubtree(root.right,subRoot)) 



    def isSameTree(self,root,subTree):
        if not root and not subTree:
            return True

        if root and subTree and root.val == subTree.val:
            return (self.isSameTree(root.left,subTree.left) and
                     self.isSameTree(root.right,subTree.right))
        return False

