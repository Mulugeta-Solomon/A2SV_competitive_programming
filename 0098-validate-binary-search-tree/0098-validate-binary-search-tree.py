# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def BST(root, max_val = float('inf'), min_val = float('-inf')):
            if root is None:
                return True 
            
            if root.val >= max_val or root.val <= min_val:
                return False 
            
            return BST(root.left, root.val, min_val) and BST(root.right, max_val, root.val)
            
        return BST(root)
    

        