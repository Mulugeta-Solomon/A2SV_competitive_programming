# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(curr):
            if len(curr) % 2:
                return False
            left, right = 0, len(curr) - 1
            while left < right:
                if curr[left][0] != curr[right][0] or curr[left][1] == curr[right][1] or curr[left][2] != curr[right][2]:
                    return False
                left += 1
                right -= 1
            
            return True
        
        queue = deque([root])

        while queue:
            size, curr = len(queue), []
            for _ in range(size):
                node = queue.popleft()

                if node.left:
                    curr.append([node.left.val, 0, node.val])
                    queue.append(node.left)
                if node.right:
                    curr.append([node.right.val, 1, node.val])
                    queue.append(node.right)
            
            if not check(curr):
                return False
        
        return True