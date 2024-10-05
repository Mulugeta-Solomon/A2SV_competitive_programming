# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []

        def length(node):
            n = 0
            while node:
                node = node.next
                n += 1
            return n
        
        result = [0] * (length(head))
        curr, i = head, 0

        while curr:
            result[i] = 0

            while stack and curr.val > stack[-1][0]:
                node = stack.pop()
                result[node[1]] = curr.val
            
            stack.append([curr.val, i])
            curr = curr.next
            i += 1

        return result 
