# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        self.max_depth, curr_depth, self.result = -1, 0, 0
        self.depthFirstSearch(root, curr_depth)
        
        return self.result
    
    def depthFirstSearch(self, root: Optional[TreeNode], curr_depth: int):

        if root is None:
            return 
        
        if curr_depth > self.max_depth:
            self.result = root.val 
            self.max_depth = curr_depth 
        
        self.depthFirstSearch(root.left, curr_depth + 1)
        self.depthFirstSearch(root.right, curr_depth + 1)

        return  
