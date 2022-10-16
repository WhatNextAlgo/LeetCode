# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0:[],1:[TreeNode()]}
        #return the list of fbt with n nodes
        def backtrack(n):
            if n  in dp:
                return dp[n]

            res = []
            for l in range(n):
                r = n - 1- l
                leftTress,rightTress =backtrack(l),backtrack(r)

                for t1 in leftTress:
                    for t2 in rightTress:
                        res.append(TreeNode(0,t1,t2))
            dp[n] = res
            return res

        return backtrack(n)
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        #return the list of fbt with n nodes
        def backtrack(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]

            res = []
            for l in range(n):
                r = n - 1- l
                leftTress,rightTress =backtrack(l),backtrack(r)

                for t1 in leftTress:
                    for t2 in rightTress:
                        res.append(TreeNode(0,t1,t2))


            return res

        return backtrack(n)





