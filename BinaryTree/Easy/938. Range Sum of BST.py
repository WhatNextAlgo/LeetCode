# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
#         ran = list(range(low,high+1))
#         total = 0
#         def get_range_sum(root):
#             nonlocal total
#             nonlocal ran

#             if root is None:
#                 return 0
#             if root.val in ran:
#                 total += root.val

#             if root.left is not None:
#                 get_range_sum(root.left)
            
#             if root.right is not None:
#                 get_range_sum(root.right)
                
#         get_range_sum(root)
#         return total
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        def get_range_sum(root,low,high):
            nonlocal total

            if root is None:
                return 0
            if root.val >= low and root.val <= 15:
                total += root.val

            if root.left is not None:
                get_range_sum(root.left,low,high)
            
            if root.right is not None:
                get_range_sum(root.right,low,high)
        get_range_sum(root,low,high)
        return total
            
        




bt = TreeNode(10)
bt.left =  TreeNode(5)
bt.right =  TreeNode(15)
bt.left.left = TreeNode(3)
bt.left.right = TreeNode(7)
#bt.right.left = TreeNode(4)
bt.right.right = TreeNode(18)
s =Solution()
print(s.rangeSumBST(bt,7,15))
