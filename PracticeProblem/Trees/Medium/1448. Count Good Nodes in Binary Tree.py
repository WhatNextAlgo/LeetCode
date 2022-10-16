# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        #preOrder traversal
        def dfs(node,maxVal):
            if not node: return 0
            res = 1 if node.val >= maxVal else 0 # compute the good node
            maxVal = max(maxVal,node.val) # compute so far max value
            res += dfs(node.left,maxVal) # traverse the left and compute good node , maxVal
            res += dfs(node.right,maxVal) # traverse the right and compute good node , maxVal
            return res # return compute result for each 
        
        return dfs(root,root.val)




s = Solution()

bt = TreeNode(3)
bt.left = TreeNode(1)
bt.right = TreeNode(4)
bt.left.left = TreeNode(3)
bt.right.left = TreeNode(1)
bt.right.right = TreeNode(5)
print(s.goodNodes(bt))