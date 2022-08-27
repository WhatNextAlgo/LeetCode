# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:return True
        if not root:return False

        if self.sameTree(root,subRoot):
            return True
        
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))


    def sameTree(self,s,t):
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            return (self.sameTree(s.left,t.left) and
                    self.sameTree(s.right,t.right))

        return False

        



    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def areIdentical(root1, root2):
            if root1 is None and  root2 is None:
                return True

            
            if  root1 and root2 and (root1.val == root2.val):
                return ((areIdentical(root1.left , root2.left)) 
            and areIdentical(root1.right , root2.right))

            return False

        def is_subtre_helper(s,t):
            if not t :return True
            if not s :return False

            if (areIdentical(s,t)):
                return True
            
            return is_subtre_helper(s.left,t) or is_subtre_helper(s.right, t)

        return is_subtre_helper(root,subRoot)

    



