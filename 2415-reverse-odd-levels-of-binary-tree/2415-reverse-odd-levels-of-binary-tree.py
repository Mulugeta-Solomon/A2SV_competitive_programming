# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Using BFS 

        queue = deque([(root, 0)])

        while queue:
            size, curr = len(queue), []
            for _ in range(size):
                node, level = queue.popleft()
                curr.append(node)

                if node.left:
                    queue.append((node.left, level + 1))
                
                if node.right:
                    queue.append((node.right, level + 1))
            
            if level % 2 == 1:
                left, right = 0, len(curr) - 1
                while left < right: # Because it is a perfect binary tree
                    curr[left].val, curr[right].val = curr[right].val, curr[left].val
                    left += 1
                    right -= 1
                
        return root 




