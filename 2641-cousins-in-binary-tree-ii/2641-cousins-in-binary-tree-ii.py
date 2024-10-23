# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        levelSum = defaultdict(int)
        queue, level = deque([root]), 0

        while queue: # BFS approach 
            size, currSum = len(queue), 0
            for _ in range(size):
                node = queue.popleft()
                currSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            levelSum[level] = currSum
            level += 1
        
        queue, level = deque([root]), 0

        while queue:
            size = len(queue) 
            for _ in range(size):
                node = queue.popleft()
                if level == 0:
                    node.val = 0
                    level += 1
                
                curr = 0
                if node.left:
                    queue.append(node.left)
                    curr += node.left.val
                if node.right:
                    queue.append(node.right)
                    curr += node.right.val
                
                if node.left:
                    node.left.val = levelSum[level] - curr
                if node.right:
                    node.right.val = levelSum[level] - curr

            level += 1            

        return root

             
        