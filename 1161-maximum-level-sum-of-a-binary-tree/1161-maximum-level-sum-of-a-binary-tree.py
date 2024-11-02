# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue, result, level = deque([root]), [float('-inf'), 0], 0

        while queue:
            size, curr = len(queue), 0
            for _ in range(size):
                node = queue.popleft()
                curr += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
            if curr > result[0]:
                result = [curr, level]
        
        return result[1]



        