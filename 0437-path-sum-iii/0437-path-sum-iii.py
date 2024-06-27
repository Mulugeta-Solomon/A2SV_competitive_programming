# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0
        def dfs_sum(root, curr):
            nonlocal result
            if not root:
                return 
            if root.val == curr:
                result += 1
            
            dfs_sum(root.left, curr - root.val)
            dfs_sum(root.right, curr - root.val)
        
        def dfs(root, target):
            if not root:
                return 
            dfs_sum(root, target)
            dfs(root.left, target)
            dfs(root.right, target)
        
        dfs(root, targetSum)
        return result 

       
        return  dfs(root, 0, result)