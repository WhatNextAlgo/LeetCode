# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #This Solution is Time Limit Exceeded
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        def dfs(n):
            if n ==0:
                return []
            if n == 1:
                return [TreeNode()]

            res = []
            for l in range(n):
                r = n -1 -l # Treeright = n -1 - leftTree
                leftTrees,rightTrees = dfs(l), dfs(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0,t1,t2))

            return res

        return dfs(n) 
    # small optimization - passed on Leetcode
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0:[],1:[TreeNode()],2:[]} # base case

        def dfs(n):
            if n in dp:
                return dp[n]

            res = []
            for l in range(n):
                r = n -1 -l # Treeright = n -1 - leftTree
                leftTrees,rightTrees = dfs(l), dfs(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0,t1,t2))
            dp[n] = res

            return res

        return dfs(n) 





