# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        result = []

        def dfs(root, curr, total):
            
            total += root.val
            if total == targetSum and (not root.left and not root.right):
                result.append(curr[:] + [root.val])
                total = 0
                return 
            
            if root.left:
                dfs(root.left, curr + [root.val], total)

            if root.right:
                dfs(root.right, curr + [root.val], total) 
        
        dfs(root, [], 0)

        return result
        