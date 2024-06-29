# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        queue = deque([(root, 0, 0)])
        result = []
        visited = [0, 1]
        visited_sofar = defaultdict(list)
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                node, level, idx = queue.popleft()
                
                if node.val == target.val:
                    visited = [level, idx]
                else:
                    visited_sofar[node.val] = [level, idx]

                if node.left:
                    queue.append((node.left, level + 1, idx * 2))
                if node.right:
                    queue.append((node.right, level + 1, idx * 2 + 1))
    

        for key in visited_sofar.keys():
            curr_level, curr_idx = visited_sofar[key]
            if curr_level != visited[0]:
                if abs(curr_level - visited[0]) == k:
                    result.append(key)
            else:
                if abs(curr_idx - visited[1]) + 1 == k:
                    result.append(key)

        
        return result 
                