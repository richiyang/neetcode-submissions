"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # oldToNew = {}

        # def dfs(node):
        #     if node in oldToNew:
        #         return oldToNew[node]

        #     copy = Node(node.val)
        #     oldToNew[node] = copy
        #     for neighbor in node.neighbors:
        #         copy.neighbors.append(dfs(neighbor))
        #     return copy
            
        # return dfs(node) if node else None

        if not node:
            return None
        
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                oldToNew[cur].neighbors.append(oldToNew[neighbor])

        return oldToNew[node]
    