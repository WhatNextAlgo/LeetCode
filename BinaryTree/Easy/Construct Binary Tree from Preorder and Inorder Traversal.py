# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

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

def preorder(root):
    if not root:
        return None
    print(root.val, end = ' ')
    if root.left is not None:
        preorder(root.left)
    else:
        print("null",end= ' ')
    if root.right is not None:
        preorder(root.right)



s = Solution()
btree = s.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
preorder(btree)


