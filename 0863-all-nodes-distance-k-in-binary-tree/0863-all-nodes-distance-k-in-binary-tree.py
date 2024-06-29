# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def bfs(root, parent):
            if not root:
                return None 
            parent_dict[root.val] = parent

            left = bfs(root.left, root)
            right = bfs(root.right, root) 

        parent_dict = defaultdict()
        bfs(root, None)
        
        result = []
        queue = deque([(target, 0)])
        visited = set()

        while queue:
            node, level = queue.popleft()

            if node.val not in visited:
                visited.add(node.val)

                if level == k:
                    result.append(node.val)
                
                if level <= k:
                    if node.left:
                        queue.append((node.left, level + 1))
                    if node.right:
                        queue.append((node.right, level + 1))
                    
                    if parent_dict[node.val]:
                        queue.append((parent_dict[node.val], level + 1))

        return result 
                