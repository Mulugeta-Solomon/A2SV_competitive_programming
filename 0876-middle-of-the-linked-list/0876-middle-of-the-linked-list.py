# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head):
        curr, size = head, 0
        
        while curr:
            curr = curr.next
            size += 1
        
        return size

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = self.length(head)
        mid = size//2 + 1 if size % 2 == 0 else -(-size//2)
        
        curr, idx = head, 0

        while idx < mid-1:
            curr = curr.next
            idx += 1
        
        return curr
        




    
