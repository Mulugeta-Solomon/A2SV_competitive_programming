# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        merge_root = TreeNode(None)
        merge_root = self.merge(root1, root2, merge_root)

        return merge_root
    
    def merge(self, root1: Optional[TreeNode], root2: Optional[TreeNode], merge_root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1 and not root2:
            return 
 
        val_1 = root1.val if root1 else 0
        val_2 = root2.val if root2 else 0
        merge_root = TreeNode(val_1 + val_2)

        merge_root.left = self.merge(root1.left if root1 else None, root2.left if root2 else None, merge_root.left)
        merge_root.right = self.merge(root1.right if root1 else None, root2.right if root2 else None, merge_root.right)

        return merge_root
        
            

            


