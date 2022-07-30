# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: 
            return []
        
        que = []
        que.append((root,str(root.val)))
        result = []
        def is_leaf_node(node):
            return not node.left and not node.right
            
        while que:
            node, path = que.pop()
            
            if is_leaf_node(node):
                result.append(path)
            
            if node.left:
                que.append((node.left, path+"->"+str(node.left.val)))
            
            if node.right:
                que.append((node.right, path+"->"+str(node.right.val)))
        
        return result


        
s = Solution()

bt = TreeNode(3)
bt.left =  TreeNode(5)
bt.right =  TreeNode(1)
bt.left.left = TreeNode(6)
bt.left.right = TreeNode(2)
bt.right.left = TreeNode(9)
bt.right.right = TreeNode(8)

print(s.binaryTreePaths(bt))
        