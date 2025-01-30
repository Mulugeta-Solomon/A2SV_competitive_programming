# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree, root, visited = {}, None, set() 
        for parent, child, isleft in descriptions:
            if parent not in tree:
                if isleft:
                    tree[parent] = [-1, child]
                else:
                    tree[parent] = [child, -1]
            else:
                tree[parent][isleft] = child
            
            visited.add(child)
        
        queue = deque()
        for parent, child in tree.items():
            if parent not in visited:
                root = parent
        
        root = TreeNode(root)
        queue.append(root)

        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr.val in tree:
                    for i, child in enumerate(tree[curr.val]):
                        if child != -1:
                            if i == 0:
                                curr.right = TreeNode(child)
                                queue.append(curr.right)
                            else:
                                curr.left = TreeNode(child)
                                queue.append(curr.left)
        
        return root
                    

        
        

        
