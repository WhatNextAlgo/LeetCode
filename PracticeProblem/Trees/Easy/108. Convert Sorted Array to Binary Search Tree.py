# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def construct_binary_tree(n):
            if n == []:
                return None
            mid = len(n)//2 # take the mid index
            root = TreeNode(n[mid]) # create the root node with mid index
            # construct BT for left portion from mid to left side
            root.left = construct_binary_tree(n[:mid]) 
            # construct BT for right portion from mid to right side
            root.right = construct_binary_tree(n[mid + 1:])
            return root
        
        return construct_binary_tree(nums)

    def display(self,root):
        if not root:return None
        print(root.val,end =" ") 
        self.display(root.left)
        self.display(root.right)


s = Solution()
print(s.display(s.sortedArrayToBST(nums = [-10,-3,0,5,9])))

