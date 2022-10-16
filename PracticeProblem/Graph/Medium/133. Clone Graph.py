
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        def clone(node):
            # if node already in hashmap then return that node
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy # old to new node in hashmap
            for nei in node.neighbors: # every single neighbors
                copy.neighbors.append(clone(nei))
            
            return copy

        return clone(node) if node else None

s = Solution()
#print(s.cloneGraph(adjList = [[2,4],[1,3],[2,4],[1,3]]))