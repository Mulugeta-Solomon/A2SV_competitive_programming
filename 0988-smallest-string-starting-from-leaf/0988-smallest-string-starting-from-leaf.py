# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node, path):
            path.append(chr(node.val + 97))
            # base case
            if not node.left and not node.right: # if leaf node
                if not result:
                    result.append(''.join(path[::-1]))
                else:
                    result[0] = min(result[0], ''.join(path[::-1]))
                return 
            
            if node.left:
                dfs(node.left, path)
                path.pop()
            if node.right:
                dfs(node.right, path)
                path.pop()
        
        result = []
        dfs(root, [])
        
        return result[0]




