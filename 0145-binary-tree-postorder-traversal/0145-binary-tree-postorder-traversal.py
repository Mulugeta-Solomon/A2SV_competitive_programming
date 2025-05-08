# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack, result_stack = [root], []

        while stack:
            node = stack.pop()
            result_stack.append(node)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return [node.val for node in reversed(result_stack)]
