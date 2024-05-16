# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return 
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        
        else: # we found the match for the key
            if root.left is None: # check for 1 child
                root = root.right
            elif root.right is None:
                root = root.left
            
            else: # both children are present 
                curr = root.right
                while curr.left: # find inorder successor
                    curr = curr.left
                
                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val) # delete the curr.val after
        
        return root
        

    
        
        
        