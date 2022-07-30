from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.preordertraversal_helper(root,[])

    
    def preordertraversal_helper(self,root,lst):
        if root is None:
            return []
        
        lst.append(root.val)
        
        if root.left is not None:
            self.preordertraversal_helper(root.left,lst)
        
        if root.right is not None:
            self.preordertraversal_helper(root.right,lst)
        
        return lst

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inordertraversal_helper(root,[])

    def inordertraversal_helper(self,root,lst):
        if root is None:
            return []
        
        if root.left is not None:
            self.inordertraversal_helper(root.left,lst)
        
        lst.append(root.val)
        
        if root.right is not None:
            self.inordertraversal_helper(root.right,lst)
        
        return lst

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postordertraversal_helper(root,[])

    def postordertraversal_helper(self,root,lst):
        if root is None:
            return []
        
        if root.left is not None:
            self.postordertraversal_helper(root.left,lst)
        
        if root.right is not None:
            self.postordertraversal_helper(root.right,lst)
        
        lst.append(root.val)
        
        return lst

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return  self.levelorder_helper(root)


    def levelorder_helper(self,root):
        q = []
        q.append(root)
        result = []
        while q != []:
            temp = []
            for _ in range(len(q)):
                poped = q.pop(0)
                temp.append(poped.val)
                if poped.left is not None:
                    q.append(poped.left)
                
                if poped.right is not None:
                    q.append(poped.right)
            result.append(temp)
        return result
            
        

    

        


bt = TreeNode(3)
bt.left =  TreeNode(1)
bt.right =  TreeNode(2)
bt.left.left = TreeNode(4)
bt.right.right = TreeNode(5)

s = Solution()
print(s.preorderTraversal(bt))
print(s.inorderTraversal(bt))
print(s.postorderTraversal(bt))
print(s.levelOrder(bt))


    