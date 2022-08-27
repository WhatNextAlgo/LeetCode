# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        q.append(root)
        result = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)
        return result
        




    def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = []
        q.append(root)
        result = []
        while q:
            level = []
            for _ in range(len(q)):
                poped = q.pop(0)
                level.append(poped.val)
                if poped.left is not None:
                    q.append(poped.left)
                
                if poped.right is not None:
                    q.append(poped.right)
            result.append(level)
        return result

    