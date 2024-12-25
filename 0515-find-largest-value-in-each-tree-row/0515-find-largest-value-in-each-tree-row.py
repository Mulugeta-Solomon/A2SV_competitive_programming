# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        queue, result = deque([root]), [root.val]

        while queue:
            size, level_max = len(queue), float('-inf')
            for _ in range(size):
                node = queue.popleft()

                if node.left:
                    level_max = max(level_max, node.left.val)
                    queue.append(node.left)
                
                if node.right:
                    level_max = max(level_max, node.right.val)
                    queue.append(node.right)

            if level_max != float('-inf'):
                result.append(level_max)
            
        return result 



        