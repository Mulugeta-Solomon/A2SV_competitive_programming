# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = self.depthFirstSearch(root, [])

        return result
    
    def depthFirstSearch(self, root: Optional[TreeNode], result: List[int]) -> List[int]:
        if root is None:
            return  
        self.depthFirstSearch(root.left, result)
        result.append(root.val)
        self.depthFirstSearch(root.right, result)

        return result