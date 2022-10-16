class Solution:
    def numTrees(self, n: int) -> int:
        """
        numTree[4] =  numTree[0] * numTree[3] +
                      numTree[1] * numTree[2] +
                      numTree[2] * numTree[1] +
                      numTree[3] * numTree[0] 
        """
        numTree = [1] * (n + 1)
        # 0 nodes = 1 tree
        # 1 nodes = 1 tree
        for nodes in range(2,n + 1):
            total = 0
            for root in range(1, nodes + 1):
                l = root - 1
                r = nodes - root
                total += numTree[l] * numTree[r]
            numTree[nodes] = total
        return numTree[n]

s = Solution()
print(s.numTrees( n = 4))