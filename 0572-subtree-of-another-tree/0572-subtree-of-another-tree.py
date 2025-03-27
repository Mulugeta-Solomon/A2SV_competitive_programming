# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(node, target):
            if not node and not target:
                return True
            
            if (node and not target) or (not node and target):
                return False

            if node.val !=  target.val:
                return False

            return is_same(node.left, target.left) and is_same(node.right, target.right) 


        queue = deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if is_same(node, subRoot):
                    return True
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return False
