# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.curr = self.new= TreeNode()

        def inorder(root):
            if root is None:
                return None
            inorder(root.left)
            new_node= TreeNode(root.val)
            self.curr.right  = new_node
            self.curr = self.curr.right
            inorder(root.right)
        

        inorder(root)
        return self.new.right




bt = TreeNode(5)
bt.left =  TreeNode(3)
bt.right =  TreeNode(6)
bt.left.left = TreeNode(2)
bt.left.right = TreeNode(4)
bt.left.left.left = TreeNode(1)
bt.right.right = TreeNode(8)

s = Solution()
s.increasingBST(bt)






        