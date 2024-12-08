# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parentLookUp = defaultdict()
        parentLookUp[root] = None

        queue = deque([root])

        while queue:
            size = len(queue)
            for _ in range(size):
                parent = queue.popleft()

                if parent.left:
                    parentLookUp[parent.left] = parent 
                    queue.append(parent.left)
                if parent.right:
                    parentLookUp[parent.right] = parent
                    queue.append(parent.right)
        
        def level(node):
            result = 0

            while parentLookUp[node] != None:
                node = parentLookUp[node]
                result += 1
            
            return result
        
        plevel, qlevel = level(p), level(q)
        DIFF = abs(plevel - qlevel)

        if plevel > qlevel:
            for _ in range(DIFF):
                p = parentLookUp[p]
        if plevel < qlevel:
            for _ in range(DIFF):
                q = parentLookUp[q]
        
        while p != q:
            p, q = parentLookUp[p], parentLookUp[q]

        return p

        return p