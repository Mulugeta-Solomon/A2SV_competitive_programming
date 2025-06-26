# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node, curr):
            curr.append(chr(node.val + 97))
            
            if not node.right and not node.left:
                # result.append(''.join(curr[:]))
                if not result:
                    result. append(''.join(curr[::-1]))
                else:
                    result[0] = min(result[0], ''.join(curr[::-1]))
                curr.pop()
                return 
        
            if node.left:
                dfs(node.left, curr)
            if node.right:
                dfs(node.right, curr)
            curr.pop()

        
        result = []
        dfs(root, [])
        
        # result = [s[::-1] for s in result]
        # result.sort()
        
        return result[0]