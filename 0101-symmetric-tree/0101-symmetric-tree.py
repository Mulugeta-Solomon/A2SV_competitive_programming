# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def ispalindrome(nums):
            left, right = 0, len(nums) - 1
            while left < right:
                if nums[left] != nums[right]:
                    return False
                left += 1
                right -= 1
            return True

        queue, levels = deque([root]), []

        while queue:
            size, curr = len(queue), []
            for _ in range(size):
                node = queue.popleft()
                if node:
                    curr.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                    continue
                curr.append(None)
            
            levels.append(curr)
        
        for level in levels:
            if not ispalindrome(level):
                return False
        
        return True