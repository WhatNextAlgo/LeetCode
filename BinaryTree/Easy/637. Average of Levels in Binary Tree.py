# Definition for a binary tree node.
from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = []
        q.append(root)
        res = []
        
        while q != []:
            total = count  = 0
            temp = []
            while q != []:
                poped = q.pop()
                total += poped.val
                count += 1
                if poped.left is not None:
                    temp.append(poped.left)
                if poped.right is not None:
                    temp.append(poped.right)
            q = temp
            res.append((total * 1.0)/count)
        return res





bt = TreeNode(3)
bt.left =  TreeNode(9)
bt.right =  TreeNode(20)
#bt.left.left = TreeNode(1)
#bt.left.right = TreeNode(3)
bt.right.left = TreeNode(15)
bt.right.right = TreeNode(7)

s = Solution()
print(s.averageOfLevels(bt) )