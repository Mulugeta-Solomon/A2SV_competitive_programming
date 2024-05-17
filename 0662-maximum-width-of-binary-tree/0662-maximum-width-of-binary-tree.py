# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        position = defaultdict(list)

        return  self.width(root, 1, 0, position, 0)
    
    def width(self, root, curr_idx, depth, position, max_width):
        if not root:
            return max_width
        
        if depth not in position:
            position[depth] = [float('inf'), float('-inf')]
        
        position[depth][0] = min(position[depth][0], curr_idx)
        position[depth][1] = max(position[depth][1], curr_idx)

        max_width = position[depth][1] - position[depth][0] + 1

        max_width = max(max_width, self.width(root.left, curr_idx * 2, depth + 1, position, max_width)) 
        max_width = max(max_width, self.width(root.right, curr_idx * 2 + 1, depth + 1, position, max_width))
        

        return max_width



        