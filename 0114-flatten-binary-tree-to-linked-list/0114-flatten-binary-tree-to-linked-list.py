# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        result = []
        def dfs(node):
            if not node:
                return 
            result.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        i = 1
        while i < len(result):
            root.left = None
            root.right = result[i]
            root = root.right
            i += 1
