# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def get_node(org,clo,target):
            if org is None:
                return None
            if org == target:
                return clo
            
            if org.left is not None:
                temp = get_node(org.left,clo.left,target)
                if temp is not None:
                    return temp
            
            if org.right is not None:
                return get_node(org.right,clo.right,target)
            
        return get_node(original,cloned,target)
            
            
                
                
        