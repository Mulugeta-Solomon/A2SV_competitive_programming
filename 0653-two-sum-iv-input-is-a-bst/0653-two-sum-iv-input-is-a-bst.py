# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue, visited = deque([root]), {}

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.val in visited:
                    if visited[node.val] + node.val == k:
                        return True
                visited[abs(node.val - k)] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
      
        return False