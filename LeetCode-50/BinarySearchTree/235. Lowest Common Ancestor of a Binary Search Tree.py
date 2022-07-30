# Definition for a binary tree node.
from more_itertools import first


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root
        first = p.val
        second = q.val
        def get_ancestor(root):
            val = root.val
            if val < min(first,second):
                return get_ancestor(root.right)
            if val > max(first,second):
                return get_ancestor(root.left)
            return root       

        return get_ancestor(root)         

        
                


    


        




bst =TreeNode(6)
left = TreeNode(2)
right = TreeNode(8)
bst.left = left
bst.right =right

left.left = TreeNode(0)
left.right = TreeNode(4)

right.left =  TreeNode(7)
right.right =TreeNode(9)

s = Solution()
print(s.lowestCommonAncestor(bst,right,right.right).val)