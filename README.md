# LeetCode

## Binary Search Tree


<details>

<summary>235.Lowest Common Ancestor of a Binary Search Tree	</summary>

```from more_itertools import first

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
```

</details>
 
 
<details>

<summary>98. Validate Binary Search Tree.</summary>

```class TreeNode:
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
```

</details>

