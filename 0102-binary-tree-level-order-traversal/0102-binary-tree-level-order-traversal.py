# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return None 
            
        queue = deque([root])
        result = []

        while queue:
            curr = []
            i = len(queue)
            while i > 0:
                node = queue.popleft()
                curr.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                i -= 1
            result.append(curr)
        
        return result 

            