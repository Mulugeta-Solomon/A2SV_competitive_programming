# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        def in_order(node):
            if not node:
                return 
            in_order(node.left)
            self.inorder.append(node.val)
            in_order(node.right)
        in_order(root)

        self.ptr = 0

    def next(self) -> int:
        curr = self.inorder[self.ptr]
        self.ptr += 1
        return curr

    def hasNext(self) -> bool:
        return self.ptr < len(self.inorder)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()