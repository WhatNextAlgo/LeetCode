# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def contruct_binary_tree(nums:List[int]) -> TreeNode:
            if nums == []:
                return None
            key = max(nums)
            index = nums.index(key)
            node = TreeNode(key)
            node.left = contruct_binary_tree(nums[:index])
            node.right = contruct_binary_tree(nums[index+1:])
            return node
        return contruct_binary_tree(nums)



s = Solution()
print(s.constructMaximumBinaryTree(nums = [3,2,1,6,0,5]))