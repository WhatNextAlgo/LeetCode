# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        
        res = []
        def inorder(root):
            if root is None:
                return 
            else:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)

        inorder(root)       
        for x in range(1,len(res)):
            if res[x] > res[x -1]:
                continue
            else:
                return False
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        tree = []
        def DFS(r) :
            if not r:
                return    
            else:
                DFS(r.left)
                tree.append(r.val)
                DFS(r.right)
        
        DFS(root)
        print(tree)
        for i in range(1 , len(tree)):
            if tree[i] > tree[i-1]: 
                continue
            else :
                return False        
        return True



        

        



# bst =TreeNode(2)
# left = TreeNode(1)
# right = TreeNode(3)
# bst.left = left
# bst.right =right

bst1 =TreeNode(2)
left = TreeNode(2)
right = TreeNode(2)
# bst1.left = left
# bst1.right =right

# right.left = TreeNode(3)
# right.right = TreeNode(7)

s = Solution()
print(s.isValidBST(bst1))
