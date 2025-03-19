# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lookup = defaultdict(int)
        queue = deque([root])

        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                lookup[curr.val] += 1
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        result = []
        for val, freq in lookup.items():
            if result:
                if result[-1][1] == freq: 
                    result.append((val, freq))
                elif result[-1][1] < freq:
                    result = [(val, freq)]
                continue
            result.append((val, freq))

        return [val for val, freq in result]