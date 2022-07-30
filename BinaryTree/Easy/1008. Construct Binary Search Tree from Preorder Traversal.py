# Definition for a binary tree node.
from multiprocessing import dummy
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if preorder == []:
                return None
        key = preorder[0]
        curr,dummy = TreeNode(key)

        
        def contruct_binary_tree(node: Optional[TreeNode],key):
            if key > node.val:
                if node.right is None:
                    node.right = TreeNode(key)
                else:
                    contruct_binary_tree(node.right,key)
            elif key < node.val:
                if node.left is None:
                    node.left =  TreeNode(key)
                else:
                    contruct_binary_tree(node.left,key)
        for x in preorder[1:]:
            contruct_binary_tree(curr,x)
        return dummy
   

        

            


            
            
        