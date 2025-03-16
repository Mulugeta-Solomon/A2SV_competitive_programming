"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue, result = deque([root]), 0

        while queue:
            size = len(queue)
            result += 1
            for _ in range(size):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
        
        return result