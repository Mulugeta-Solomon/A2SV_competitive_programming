# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        level, i, n = [], 0, len(traversal)
        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            node = 0
            while i < n and traversal[i].isdigit():
                node = node * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(node)
            
            if depth < len(level):
                level[depth] = node
            else:
                level.append(node)

            if depth > 0:
                parent = level[depth - 1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node

        return level[0] 



        
        
        # # def recur(node, idx):
        # #     for i in range(idx, len(nodes)):
        # #         if i == 1:
        # #             if not node.left:
        # #                 node.left = TreeNode(nodes[i][0])
                        
        # #                 continue
        # #             node.right = TreeNode(nodes[i][0])

        # #         if nodes[i][1] < nodes[i - 1][1]:
        # #             recur(cache[nodes[idx][1] + 1], idx)
                
        # #         if nodes[i][1] > nodes[i - 1][1]:
        # #             node = node.left
        # #             cache[] 
        # #             if not node.left:
        # #                 node.left = TreeNode(nodes[i][0])
      
        # #         else:
        # #             node.right = TreeNode(node[i][0])

        # return root
