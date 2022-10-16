class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        if not n:
            return False

        adj = { src:[] for src in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue

                if not dfs(j , i):
                    return False
            return True
        
        return dfs(0,-1) and n == len(visit)



s = Solution()
print(s.validTree(n=5,edges= [[0,1],[0,2],[0,3],[1,4]]))