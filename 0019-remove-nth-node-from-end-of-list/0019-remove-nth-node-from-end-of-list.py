# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head):
        size, curr = 0, head
        while curr:
            curr = curr.next
            size += 1
        
        return size
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        size = self.length(head)

        dummy = ListNode(0)
        dummy.next = head
        node, idx = dummy, 0

        while idx < size - n:
            node = node.next
            idx += 1

        node.next = node.next.next

        return dummy.next

      

 