"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        all_nodes = {}
        all_nodes[node.val] = Node(val=node.val)
        q = collections.deque([node])
     
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                
                if neighbor.val not in all_nodes:
                    all_nodes[neighbor.val] = Node(val=neighbor.val)
                    q.append(neighbor)
                
                all_nodes[n.val].neighbors.append(all_nodes[neighbor.val])
                    
        
        return all_nodes[node.val]
            

        