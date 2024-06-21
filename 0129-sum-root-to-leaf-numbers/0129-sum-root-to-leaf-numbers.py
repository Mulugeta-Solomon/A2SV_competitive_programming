# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths, total = [], 0

        def dfs(root, path):
            if not root:
                return 

            path += str(root.val)
            if not (root.left or root.right):
                paths.append(path)
                return

            dfs(root.left, path)
            dfs(root.right, path)

        dfs(root, '')
        for val in paths:
            total += int(val)

        return total
        