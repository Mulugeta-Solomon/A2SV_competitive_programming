# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, curr):
            if not node:
                return 
            
            curr += str(node.val)
            if not node.left and not node.right:
                result.append(curr)
            else:
                curr += '->'
                dfs(node.left, curr)
                dfs(node.right, curr)
        
        result = []
        dfs(root, '')

        return result 