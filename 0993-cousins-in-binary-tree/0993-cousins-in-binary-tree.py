# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False

        queue, depth = deque([root]), 0
        x, y = [x, None, None, 0], [y, None, None, 0] # [x, parent, depth, found]

        while queue:
            size = len(queue)
            depth += 1
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    if node.left.val == x[0]:
                        x = [x, node, depth, 1]
                    if node.left.val == y[0]:
                        y = [y, node, depth, 1]
                    queue.append(node.left)
                if node.right:
                    if node.right.val == x[0]:
                        x = [x, node, depth, 1]
                    if node.right.val == y[0]:
                        y = [y, node, depth, 1]
                    queue.append(node.right)

                if x[3] and y[3]:
                    if x[1] != y[1]:
                        return x[2] == y[2]
                    return False
        return False
