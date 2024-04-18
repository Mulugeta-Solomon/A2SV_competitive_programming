# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head 
        
        size, curr, start = 1, head, head 

        while curr.next:
            curr = curr.next
            size += 1
        
        curr.next = head 
        k = k % size
        k = size - k

        while k > 0:
            start = start.next
            curr = curr.next
            k -= 1
        curr.next = None
        
        return start

