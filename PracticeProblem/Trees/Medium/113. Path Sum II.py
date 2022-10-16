# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node,curSum,path):
            nonlocal res
            if not node:
                return None

            curSum += node.val
            path.append(node.val)
            
            if not node.left and not node.right:
                if curSum == targetSum:
                    res.append(path.copy())
    

            
            dfs(node.left,curSum,path)
            dfs(node.right,curSum,path)
            path.pop(node.val)

        dfs(root, 0,[])
        return res




s = Solution()
bt = TreeNode(5)
bt.left = TreeNode(4)
bt.right = TreeNode(8)
bt.left.left = TreeNode(4)
bt.left.left = TreeNode(11)
bt.left.left.left = TreeNode(7)
bt.left.left.right = TreeNode(2)
bt.right.left = TreeNode(13)
bt.right.right = TreeNode(4)
bt.right.right.left = TreeNode(5)
bt.right.right.right = TreeNode(1)

print(s.pathSum(bt,22))
        