# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = [0]
        def dfs(node):
            if not node:
                return 0, 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            total = left[0] + right[0] + node.val
            count = left[1] + right[1] + 1

            if total // count == node.val:
                result[0] += 1
            
            return total, count

        dfs(root)

        return result[0]  