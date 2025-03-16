# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        node_val, queue, result = [], deque([root]), float('inf')
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                node_val.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        node_val.sort()
        for i in range(1, len(node_val)):
            result = min(result, node_val[i] - node_val[i-1])

        return result