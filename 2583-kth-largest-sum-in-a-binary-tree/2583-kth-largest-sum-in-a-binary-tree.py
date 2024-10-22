# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        queue, levelSum = deque([root]), []

        while queue:
            size, curr = len(queue), 0
            for _ in range(size):
                node = queue.popleft()
                curr += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            levelSum.append(curr)
        
        
        if len(levelSum) < k:
            return -1

        levelSum.sort()

        return levelSum[len(levelSum) - k]

