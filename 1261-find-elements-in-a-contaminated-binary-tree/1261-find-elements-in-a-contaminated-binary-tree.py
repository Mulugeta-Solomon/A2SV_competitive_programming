# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        queue = deque([self.root])

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    node.left.val = 2 * node.val + 1
                    queue.append(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    queue.append(node.right)
    

    def find(self, target: int) -> bool:

        queue = deque([self.root])

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()

                if node.val == target:
                    return True
                
                if node.val > target:
                    return False
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return False
                



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)