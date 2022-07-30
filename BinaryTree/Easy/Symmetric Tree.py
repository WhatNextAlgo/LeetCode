# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        print(self.left_subtree(root.left,[]))
        print(self.right_subtree(root.right,[]))
        return self.left_subtree(root.left,[]) == self.right_subtree(root.right,[])

    def right_subtree(self,root,lst):
        if root is None:
            return None
        lst.append(root.val)
        if root.right is not None:
            self.right_subtree(root.right,lst)
        else:
            lst.append(None)
        
        if root.left is not None:
            self.right_subtree(root.left,lst)
        else:
            lst.append(None)
        return lst

    def left_subtree(self,root,lst):
        if root is None:
            return None
        lst.append(root.val)
        if root.left is not None:
            self.left_subtree(root.left,lst)
        else:
            lst.append(None)
        
        if root.right is not None:
            self.left_subtree(root.right,lst)
        else:
            lst.append(None)
        return lst

        
        







bt = TreeNode(1)
bt.left =  TreeNode(2)
bt.right =  TreeNode(2)
bt.left.left = TreeNode(3)
bt.left.right = TreeNode(4)
bt.right.left = TreeNode(4)
bt.right.right = TreeNode(3)

bt = TreeNode(1)
bt.left =  TreeNode(2)
bt.right =  TreeNode(2)
bt.left.right = TreeNode(3)
bt.right.right = TreeNode(3)

s = Solution()
print(s.isSymmetric(bt))