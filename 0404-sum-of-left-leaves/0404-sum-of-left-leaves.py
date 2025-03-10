# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right): 
            return 0
        queue, result = deque([(root, False)]), 0

        while queue:
            size = len(queue)
            for _ in range(size):
                curr, left = queue.popleft()
                if left and (not curr.left and not curr.right):
                    result += curr.val
                
                if curr.left:
                    queue.append((curr.left, True))
                if curr.right:
                    queue.append((curr.right, False))
        
        return result