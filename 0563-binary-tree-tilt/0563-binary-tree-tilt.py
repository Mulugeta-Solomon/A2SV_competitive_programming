# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        result = [0]
        def dfs(node):
            if not node:
                return 0  
            left = dfs(node.left)
            right = dfs(node.right)
            curr = abs(left - right)
            result[0] += curr

            return left + right + node.val
            
        dfs(root)
        return result[0]