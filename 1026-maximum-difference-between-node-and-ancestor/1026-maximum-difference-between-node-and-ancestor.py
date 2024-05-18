# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        min_val, max_val, self.diff = root.val, root.val, float('-inf')

        return self.dfs(root, min_val, max_val)
    
    def dfs(self, root, min_val, max_val):
        if not root:
            return 

        min_val = min(min_val, root.val)
        max_val = max(max_val, root.val)
        
        self.diff = max(self.diff, max_val - min_val)
         
        self.dfs(root.left, min_val, max_val)
        self.dfs(root.right, min_val, max_val)

        return self.diff 
        

        