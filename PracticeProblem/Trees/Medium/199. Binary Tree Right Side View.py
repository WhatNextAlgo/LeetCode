# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        max_level =[0]
        def right_side_helper(root,level,max_level) -> None:
            if root is None :return None
            if max_level[0] < level:
                res.append(root.val)
                max_level[0] = level

            right_side_helper(root.right,level + 1,max_level)
            right_side_helper(root.left,level + 1,max_level)
        
        
        right_side_helper(root,1,max_level)
                
        return res
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        while q:
            rightSide = None
            qLen = len(q)
            for i  in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
