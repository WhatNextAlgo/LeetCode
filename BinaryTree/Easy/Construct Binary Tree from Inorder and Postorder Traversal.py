# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder == [] or postorder == []:
            return None

        key = postorder[-1]
        node = TreeNode(key)
        index = inorder.index(key)
        node.left = self.buildTree(inorder[:index],postorder[:index])
        node.right = self.buildTree(inorder[index+1:],postorder[index:-1])
        return node

    

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
btree = s.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])
preorder(btree)