# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def contruct_binary_tree(nums):
            mid = len(nums)//2
            key = nums[mid]
            node = TreeNode(key)
            node.left = contruct_binary_tree(nums[:mid])
            node.right = contruct_binary_tree(nums[mid+1:])
            return node
        return contruct_binary_tree(nums)
        
