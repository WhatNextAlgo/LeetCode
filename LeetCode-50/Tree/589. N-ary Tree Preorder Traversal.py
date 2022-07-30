"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List


class Solution:
    def preorder(self, root) -> List[int]:
        res =[]
        def preorder(root):
            if root is None:
                return None
            res.append(root.val)
            for child in root.children:
                preorder(child)

        preorder(root)
        return res
        
   
        
