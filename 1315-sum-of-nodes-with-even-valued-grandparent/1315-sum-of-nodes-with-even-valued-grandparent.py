# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def sum_(root):
            if not root:
                return 0
            curr = 0
            if root.left:
                curr += root.left.val
            if root.right:
                curr += root.right.val
            
            return curr

        def dfs(root):
            if not root: # base case
                return 0
            
            if root.val % 2 == 0:
                return sum_(root.left) + sum_(root.right) + dfs(root.left) + dfs(root.right)
            else:
                return dfs(root.left) + dfs(root.right)

        return dfs(root)
        