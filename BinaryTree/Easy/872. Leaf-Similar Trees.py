# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def is_leaf_node(node):
            return not node.left and not node.right

        res1 = []
        res2 = []
        def get_leaf_node(node,res):
            if node is None:
                return None

            if is_leaf_node(node):
                res.append(node.val)
            get_leaf_node(node.left,res)
            get_leaf_node(node.right,res)

        get_leaf_node(root1,res1)
        get_leaf_node(root2,res2)
        print(res1,res2)
        if len(res1) == len(res2):
            for x,y in zip(res1,res2):
                if x !=y:
                    return False
            else:
                return True
        else:
            False


s = Solution()

# bt = TreeNode(3)
# bt.left =  TreeNode(5)
# bt.right =  TreeNode(1)
# bt.left.left = TreeNode(6)
# bt.left.right = TreeNode(2)
# bt.right.left = TreeNode(9)
# bt.right.right = TreeNode(8)
bt = TreeNode(1)
bt.left =  TreeNode(2)
bt.right =  TreeNode(3)

bt1 = TreeNode(1)
bt1.left =  TreeNode(3)
bt1.right =  TreeNode(2)


print(s.leafSimilar(bt,bt1))
        