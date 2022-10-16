""" 
Each value is a root not
                LEFT     *     RIGHT
numTree[4] =  numTree[0] * numTree[3] +
                numTree[1] * numTree[2] +
                numTree[2] * numTree[1] +
                numTree[3] * numTree[0] 
"""

class Solution:
    def numTrees(self, n: int) -> int:
        numTree= [1] * (n + 1)
        # 0 node = 1 tree
        # 1 node = 1 tree
        for nodes in range(2,n +1):
            total = 0
            for root in range(1,nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        print(numTree)
        return numTree[n]


s = Solution()
print(s.numTrees(n = 3))

