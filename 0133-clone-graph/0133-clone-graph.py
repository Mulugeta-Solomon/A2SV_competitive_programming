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
        
        result = {node.val: Node(node.val, [])}
        queue = deque([node])

        while queue: 
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                curr_clone = result[curr.val]

                for neighbor in curr.neighbors:
                    if neighbor.val not in result:
                        result[neighbor.val] = Node(neighbor.val, [])
                        queue.append(neighbor)
                    curr_clone.neighbors.append(result[neighbor.val])
        
        return result[node.val]