# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, curr):
            if not root:
                return

            if root.val >= curr:
                curr = root.val
                self.result += 1

            if root.left:
                dfs(root.left, curr)
            if root.right:
                dfs(root.right, curr)
        
        self.result = 0
        dfs(root, root.val)

        return self.result 
