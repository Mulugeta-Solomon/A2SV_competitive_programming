# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = deque([root])
    
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node and (node.left or node.right):
                    node.left, node.right = node.right, node.left
                    queue.append((node.left))
                    queue.append(node.right)

        return root