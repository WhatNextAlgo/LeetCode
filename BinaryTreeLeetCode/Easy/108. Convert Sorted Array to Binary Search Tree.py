# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(l,r):
            if l > r:
                return None
            
            m = (l + r)//2
            root = TreeNode(nums[m])
            root.left = helper(l,m-1)
            root.right = helper(m + 1,r)
            return root
        return helper(0,len(nums)-1)


s = Solution()
print(s.sortedArrayToBST(nums = [-10,-3,0,5,9]))