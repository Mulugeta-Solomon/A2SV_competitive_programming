# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def dfs(node, curr):          
            if not node or node.val != curr.val :
                return False
                
            if not curr.next:
                return True

            return dfs(node.left, curr.next) or dfs(node.right, curr.next)
        
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.val == head.val and dfs(node, head):
                    return True
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return False
