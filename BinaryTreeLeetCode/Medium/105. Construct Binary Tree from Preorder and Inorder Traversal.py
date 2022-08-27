# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
            if not preorder or not inorder:
                return None
            
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:mid + 1],inorder[:mid])
            root.right = self.buildTree(preorder[mid + 1:],inorder[mid + 1:])


    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    
        def lst_to_tree(left, right):
            nonlocal preorder_index
            if left > right: return None

            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            index = inorder.index(root_value)

            preorder_index += 1


            root.left = lst_to_tree(left, index - 1)
            root.right = lst_to_tree(index + 1, right)

            return root

        preorder_index = 0

        return lst_to_tree(0, len(preorder) - 1)
