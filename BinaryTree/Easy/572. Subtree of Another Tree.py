# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def areIdentical(root1, root2):
            if root1 is None and  root2 is None:
                return True

            
            if root1 and root2 and (root1.val == root2.val):
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

                
        
bt = TreeNode(3)
bt.left =  TreeNode(4)
bt.right =  TreeNode(5)
bt.left.left = TreeNode(1)
bt.left.right = TreeNode(2)

bt1 = TreeNode(4)
bt.left =  TreeNode(1)
bt.right =  TreeNode(2)
s =  Solution()
print(s.isSubtree(bt, bt1))

        