# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def tilt_helper(root,res):
            if not root: 
                return 0
                
            left = tilt_helper(root.left,res)
            right = tilt_helper(root.right,res)

            res[0] += abs(left-right)

            return left + right + root.val

        tilt_helper(root,res)
        return res[0]
        
            
            
bt = TreeNode(4)     
bt.left = TreeNode(2)    
bt.right = TreeNode(9)      

bt.left.left = TreeNode(3)    
bt.left.right = TreeNode(5)   

bt.right.right = TreeNode(7)      
            

s = Solution()
print(s.findTilt(bt))
