# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.max_depth_helper(root)

    # Solution 1
    def max_depth_helper(self,root):
        if not root:
            return 0

        return 1 + (max(self.max_depth_helper(root.left),
                    self.max_depth_helper(root.right)))

    # Solution 2
    def bfs(self,root):
        if not root:
            return 0
        level = 1
        q = [root]
        while q :
            for i in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level

    # Solution 2
    def iterative_dfs(root):
        
        stack = [[root,1]]
        res = 0
        while stack:
            node,depth = stack.pop()
            if node:
                res = max(res,depth)
                stack.append([node.left,depth + 1])
                stack.append([node.right,depth + 1])
        return res

