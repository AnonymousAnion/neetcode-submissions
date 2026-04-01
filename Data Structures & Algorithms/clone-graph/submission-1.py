"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:

            return None
        
        # BFS Search
        new_nodes = dict()
        queue = deque()
        queue.append(node)
        new_nodes.update({node.val: Node(node.val)})

        while queue:

            current_node = queue.popleft()
            new_node = new_nodes[current_node.val]
            
            for neighbor in current_node.neighbors:

                if neighbor.val not in new_nodes:

                    new_neighbor = Node(neighbor.val)
                    new_nodes.update({neighbor.val: new_neighbor})
                    queue.append(neighbor)

                else:

                    new_neighbor = new_nodes[neighbor.val]

                new_node.neighbors.append(new_neighbor)

        return new_nodes[node.val]