# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        queue, heap = deque([root]), []

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                heappush(heap, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        first, second = heappop(heap), float('-inf') 
        while heap:
            second = heappop(heap)
            if second > first:
                return second
        
        return -1
