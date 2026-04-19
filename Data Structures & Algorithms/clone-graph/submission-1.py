"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.mapping = {}

        def dfs(curr_node):
            if not curr_node:
                return None
            # don't forget the loop in mapping
            if curr_node in self.mapping:
                return self.mapping[curr_node]
            
            new_node = Node(curr_node.val)
            self.mapping[curr_node] = new_node 
            for next_node in curr_node.neighbors:
                new_node.neighbors.append(dfs(next_node))
            return new_node

        if not node:
            return None
        
        return dfs(node)
   



