# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr, prev = head.next, head

        while curr:
            if curr.val != prev.val:
                prev.next = curr
                prev = prev.next
            curr = curr.next 
            
        prev.next = None


        return head
