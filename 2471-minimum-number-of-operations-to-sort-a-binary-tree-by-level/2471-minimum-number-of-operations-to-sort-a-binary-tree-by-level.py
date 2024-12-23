# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        def min_swap(arr: List[int])-> int:
            swap, lookUp, min_heap = 0, {arr[i]: i for i in range(len(arr))}, arr[:]
            heapify(min_heap)

            for i in range(len(arr)):
                curr_small = heappop(min_heap)

                if arr[i] != curr_small:
                    temp = arr[i]
                    arr[i], arr[lookUp[curr_small]] = arr[lookUp[curr_small]], arr[i]
                    lookUp[curr_small], lookUp[temp] = lookUp[temp], lookUp[curr_small]
                    swap += 1

            return swap
        
        queue, result = deque([root]), 0

        while queue:
            size, curr_level = len(queue), []
            for _ in range(size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    curr_level.append(node.left.val)
                
                if node.right:
                    queue.append(node.right)
                    curr_level.append(node.right.val)
            
            result += min_swap(curr_level)
        
        return result