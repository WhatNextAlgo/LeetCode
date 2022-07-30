"""
# Definition for a Node.

"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def posterorder_helper(root):
            if root is None:
                return None
            
            for child in root.children:
                posterorder_helper(child)
            
            res.append(root.val)
        posterorder_helper(root)
        return res




if __name__ == "__main__":
    s = Solution()
    

    # t = Node(1)
    # three = Node(3)
    # t.children([three,Node(2),Node(4)])
    # three.children([Node(5),Node(6)])
    # s.postorder(t)

        