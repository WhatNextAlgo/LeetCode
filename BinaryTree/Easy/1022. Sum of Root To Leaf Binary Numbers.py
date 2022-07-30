# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def is_leafnode(node):
            return not node.left and not node.right
            
        def preorder(r, curr_number):
            nonlocal root_to_leaf
            if r:
                curr_number = (curr_number << 1) | r.val
                print(curr_number)
                if is_leafnode(r):
                    root_to_leaf += curr_number
                    
                preorder(r.left, curr_number)
                preorder(r.right, curr_number) 
        
        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf
                








bt = TreeNode(1)
bt.left =  TreeNode(0)
bt.right =  TreeNode(1)
bt.left.left = TreeNode(0)
bt.left.right = TreeNode(1)
bt.right.left = TreeNode(0)
bt.right.right = TreeNode(1)

s = Solution()
print(s.sumRootToLeaf(bt))