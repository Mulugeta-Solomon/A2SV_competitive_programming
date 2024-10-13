# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(node, arr):
            if not node.left and not node.right:
                arr.append(node.val)
                return arr
            
            if node.left:
                dfs(node.left, arr)
            if node.right:
                dfs(node.right, arr)

            return arr
        
        temp1 = dfs(root1, [])
        temp2 = dfs(root2, [])

        if len(temp1) != len(temp2):
            return False
        
        for i in range(len(temp1)):
            if temp1[i] != temp2[i]:
                return False

        return True
            
