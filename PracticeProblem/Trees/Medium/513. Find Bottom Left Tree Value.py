# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # problem is solved by using BFS but adding a node from right to left
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node.right: q.append(node.right)
                
            if node.left:q.append(node.left)
        return node.val



s = Solution()
bt = TreeNode(1)
bt.left = TreeNode(2)
bt.right = TreeNode(3)
bt.left.left = TreeNode(4)
bt.right.left = TreeNode(5)
bt.right.right = TreeNode(6)
bt.right.left.left = TreeNode(7)

print(s.findBottomLeftValue(bt))