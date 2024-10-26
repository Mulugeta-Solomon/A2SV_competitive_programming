# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        result, height_cache = {}, {}


        def height_(node): # height of the Tree
            if not node:
                return -1

            if node in height_cache:
                return height_cache[node]

            height = 1 + max(height_(node.left), height_(node.right))
            height_cache[node] = height
            return height

        def dfs(node, depth, max_val): # max value after removing the subtree
            if not node:
                return

            result[node.val] = max_val

            dfs(node.left, depth + 1, max(max_val, depth + 1 + height_(node.right)))
            dfs(node.right, depth + 1, max(max_val, depth + 1 + height_(node.left)))

        dfs(root, 0, 0)

        return [result[node] for node in queries]
